"""Download public originals without replacing preserved snapshots.

Does not download the section ZIP or the national TSE munzona archives.
A new acquisition log is appended to data/download-attempts.json.
data/download-manifest.json stays as the historical record.
"""
import urllib.request,gzip,json,hashlib,datetime,pathlib,concurrent.futures
P=pathlib.Path(__file__).resolve().parents[1]
sources={
'ibge-municipios.json':'https://servicodados.ibge.gov.br/api/v1/localidades/estados/33/municipios',
'ibge-malha.json':'https://servicodados.ibge.gov.br/api/v3/malhas/estados/33?formato=application/vnd.geo+json&qualidade=minima&intrarregiao=municipio',
'parana-setembro.pdf':'https://paranapesquisas.com.br/wp-content/uploads/2026/09/RJ_Set26.pdf',
'atlas-setembro.pdf':'https://cdn1.atlasintel.org/pesquisa_atlas__eleicoes_rio_de_janeiro_2026__260928_692ebb57cee1632a.pdf',
'datafolha-outubro.pdf':'https://media.folha.uol.com.br/datafolha/2026/10/02/n99iwiwkfastqk40w8-wzdovosu-7-st-wj-w16-788.pdf',
'datafolha-outubro.html':'https://datafolha.folha.uol.com.br/eleicoes/2026/10/eduardo-paes-psd-mantem-a-lideranca-com-47-dos-votos-validos-douglas-ruas-pl-cresce-e-alcanca-35.shtml',
'tre-retotalizacao.html':'https://www.tre-rj.jus.br/comunicacao/noticias/2026/Outubro/retotalizacao-de-votos-aponta-douglas-ruas-como-vencedor-no-primeiro-turno-para-o-governo-do-rj',
'tre-proclamacao.html':'https://www.tre-rj.jus.br/comunicacao/noticias/2026/Outubro/tre-rj-proclama-douglas-ruas-pl-governador-eleito',
'senado-julgamento.html':'https://www12.senado.leg.br/noticias/materias/2026/10/08/rio-de-janeiro-garotinho-tem-votos-anulados-e-douglas-ruas-sera-declarado-governador-eleito',
'quaest-final-cnn.html':'https://www.cnnbrasil.com.br/eleicoes/quaest-eduardo-paes-tem-49-no-1o-turno-no-rj-douglas-ruas-40/',
'wladimir-apoio.html':'https://www.nfnoticias.com.br/noticia-56820/eleito-deputado-federal-wladimir-garotinho-declara-apoio-a-douglas-ruas-no-20-turno-no-rj',
'prefeitos.html':'https://exame.com/brasil/disputa-por-prefeitos-acirra-corrida-ao-governo-do-rio-entre-paes-e-douglas-ruas/',
'garotinho-apoios.html':'https://www.cnnbrasil.com.br/eleicoes/garotinho-rejeita-paes-pondera-sobre-ruas-e-enfrenta-reves-na-justica/',
'lupa-sabatinas.html':'https://www.agencialupa.org/checagem/2026/09/11/em-sabatina-ruas-e-paes-omitem-processos-e-tiram-de-contexto-dados-sobre-o-rio/',
'acao-novembro.html':'https://www.cnnbrasil.com.br/eleicoes/eduardo-paes-pede-ao-tre-rj-cassacao-de-chapa-de-douglas-ruas/'
}
def get(item):
 name,url=item; record={'file':'raw/'+name,'url':url,'obtained_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  response=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=45);b=response.read()
  record['content_encoding']=response.headers.get('Content-Encoding');record['final_url']=response.url
  if b[:2]==b'\x1f\x8b':b=gzip.decompress(b)
  digest=hashlib.sha256(b).hexdigest(); dest=P/'raw'/name
  record.update(bytes=len(b),sha256=digest)
  if dest.exists():
   previous=hashlib.sha256(dest.read_bytes()).hexdigest(); record['previous_sha256']=previous
   if previous==digest:record.update(status='unchanged',note='snapshot existente preservado; bytes iguais')
   else:
    side=P/'raw'/f'{name}.versao-nova-{digest[:8]}'; side.write_bytes(b)
    record.update(status='diverged-preserved',saved_as=str(side.relative_to(P)),note='snapshot anterior preservado; versao nova gravada ao lado')
  else:(P/'raw'/name).write_bytes(b);record.update(status='downloaded')
 except Exception as e:record.update(status='failed',error=str(e))
 return record
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:records=list(pool.map(get,sources.items()))
log=P/'data'/'download-attempts.json'; attempts=json.loads(log.read_text()) if log.exists() else []
attempts.append({'executed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'records':records})
log.write_text(json.dumps(attempts,ensure_ascii=False,indent=2))
for r in records:print(r['file'],r['status'],r.get('bytes',r.get('error')))
