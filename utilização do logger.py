import logging

# Configuração básica do logger
logging.basicConfig(
    filename='log.txt',       # Nome do arquivo de log
    filemode='a',             # Modo de abertura do arquivo: 'a' para anexar, 'w' para sobrescrever
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato da mensagem de log
    level=logging.DEBUG,       # Nível mínimo de mensagem que será registrada
    encoding='utf-8'          # Codificação do arquivo de log
)

# Exemplo de uso do logger
logging.debug('Esta é uma mensagem de DEBUG, usada para diagnóstico.')
logging.info('Esta é uma mensagem de INFO, informando que o código está funcionando como esperado.')
logging.warning('Esta é uma mensagem de WARNING, indicando um possível problema.')
logging.error('Esta é uma mensagem de ERROR, indicando uma falha no programa.')
logging.critical('Esta é uma mensagem de CRITICAL, indicando um erro crítico que pode resultar em falha total.')

# Mensagem adicional para ilustrar uso contínuo
try:
    1 / 0  # Provoca um erro de divisão por zero
except ZeroDivisionError as e:
    logging.error("Erro de divisão por zero: %s", e)
    
document.getElementsByTagName('iframe')[0].src = document.getElementsByTagName('iframe')[0].src;
