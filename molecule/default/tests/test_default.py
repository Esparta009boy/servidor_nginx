import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_nginx_instalado_e_rodando(host):
    # 1. Verifica se o pacote nginx está instalado
    nginx_pkg = host.package("nginx")
    assert nginx_pkg.is_installed

    # 2. Verifica se o serviço nginx está rodando e habilitado
    nginx_service = host.service("nginx")
    assert nginx_service.is_running
    assert nginx_service.is_enabled

    # 3. Verifica se a porta 80 TCP está escutando conexões
    nginx_socket = host.socket("tcp://0.0.0.0:80")
    assert nginx_socket.is_listening