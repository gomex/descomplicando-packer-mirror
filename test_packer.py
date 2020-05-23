def test_nginx_socker_listening(host):
    nginx = host.socket('tcp://0.0.0.0:80')
    assert nginx.is_listening