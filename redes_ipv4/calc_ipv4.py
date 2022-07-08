import re


class CalcIPv4:
    """Calcula redes IPv4."""

    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

        self._definir_broadcast()
        self._definir_rede()

    @property
    def rede(self):
        return self._rede

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def numero_ips(self):
        return self._obter_numero_ips()

    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def prefixo(self):
        return self._prefixo

    @ip.setter
    def ip(self, valor):
        if not self._valida_ip(valor):
            raise ValueError('IP inválido!')

        self._ip = valor
        self._ip_binario = self._ip_para_binario(valor)

    @mascara.setter
    def mascara(self, valor):
        if not valor:
            return

        if not self._valida_ip(valor):
            raise ValueError('Máscara inválido!')

        self._mascara = valor
        self._mascara_binario = self._ip_para_binario(valor)

        # Se não foi configurado o prefixo, configura. Se já foi, não acontece nada
        if not hasattr(self, 'prefixo'):
            self.prefixo = self._mascara_binario.count('1')

    @prefixo.setter
    def prefixo(self, valor):
        if not valor:
            return

        if not isinstance(valor, int):
            raise TypeError('Prefixo precisa ser inteiro!')

        if valor > 32:
            raise TypeError('Prefixo precisa ter 32 Bits!')

        self._prefixo = valor
        self._mascara_binario = (valor * '1').ljust(32, '0')

        # Se não foi configurada a máscara, configura. Se já foi, não acontece nada
        if not hasattr(self, 'mascara'):
            self.mascara = self._binario_para_ip(self._mascara_binario)

    @staticmethod
    def _valida_ip(ip):
        """Valida um ip."""

        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_para_binario(ip):
        """Transforma o ip/máscara para binário"""

        blocos = ip.split('.')

        # Transforma os blocos em binários e preenche os octetos com 0
        blocos_binarios = [bin(int(x))[2:].zfill(8) for x in blocos]

        return ''.join(blocos_binarios)

    @staticmethod
    def _binario_para_ip(ip):
        """Transforma número binário para ip."""

        n = 8
        blocos = [str(int(ip[i:n + i], 2)) for i in range(0, 32, n)]
        return '.'.join(blocos)

    def _definir_broadcast(self):
        """Define o broadcast da rede."""

        host_bits = 32 - self.prefixo
        self._broadcast_binario = self._ip_binario[:self.prefixo] + (host_bits * '1')
        self._broadcast = self._binario_para_ip(self._broadcast_binario)

        return self._broadcast

    def _definir_rede(self):
        """Define a rede."""

        host_bits = 32 - self.prefixo
        self._rede_binario = self._ip_binario[:self.prefixo] + (host_bits * '0')
        self._rede = self._binario_para_ip(self._rede_binario)

        return self._rede

    def _obter_numero_ips(self):
        return 2 ** (32 - self.prefixo)
