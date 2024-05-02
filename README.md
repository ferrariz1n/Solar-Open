![Logo](logo.png)

# Solar-Open: Monitoramento de Energia Solar

O Solar-Open é um aplicativo web simples e eficiente que permite o monitoramento e controle da produção de energia solar de forma intuitiva e acessível tanto para usuários individuais quanto para empresas.

## Funcionalidades
**1. Cadastro de Usuário:**
- Permite que tanto usuários individuais quanto empresas se registrem no sistema.
- Os usuários devem fornecer informações como nome, endereço de e-mail e senha.
- Realiza validação do endereço de e-mail e garanta senhas seguras para todos os tipos de usuários.

**2. Login de Usuário:**
- Usuários individuais e empresas registrados podem fazer login no sistema usando seu endereço de e-mail e senha.

**3. Monitoramento de Painéis:**
- Desenvolve uma seção no aplicativo para monitorar a geração diária de energia solar e o saldo acumulado.
- Permite que empresas criem perfis de diferentes locais ou instalações para monitorar a produção de energia em várias instalações.

**4. Gerenciamento de Painéis:**
- Implementa a funcionalidade de adicionar painéis solares ao sistema.
- Tanto usuários individuais quanto empresas podem registrar novos painéis.
- Disponibiliza uma lista de todos os painéis que cada usuário possui, com opções de filtro por nome e capacidade de geração.

**5. Edição e Exclusão de Painéis:**
- Permite que os usuários editem os detalhes de painéis existentes ou os excluam conforme necessário.

**6. Notificações e Alertas:**
- Configura o sistema para enviar notificações por e-mail ou notificações push em caso de queda na geração de energia ou interrupção total da geração.
- Para empresas, possibilita a configuração de alertas específicos para cada local ou instalação.

**7. Comercialização de Créditos:**
- Cria uma loja virtual dentro do aplicativo onde os usuários, incluindo empresas, podem anunciar, vender e comprar créditos de energia gerados.
- Implementa um sistema de pagamento seguro para transações comerciais.

## Requisitos Não Funcionais
**Segurança:**
- Os dados dos usuários são armazenados de forma segura, com criptografia para proteção.
- Medidas de autenticação rigorosas são implementadas para proteger contra acessos não autorizados.

**Desempenho:**
- O aplicativo é responsivo e escalável, capaz de lidar com um grande número de usuários e locais simultaneamente.
- Consultas de banco de dados são otimizadas para garantir um desempenho rápido.

**Usabilidade:**
- A interface de usuário é intuitiva e fácil de usar em dispositivos desktop.
- O aplicativo é compatível com navegadores populares.

**Escalabilidade:**
- O projeto é desenvolvido com escalabilidade em mente, permitindo expansão conforme a demanda cresce.

**Backup e Recuperação:**
- Um plano de backup regular é mantido para os dados do sistema, com capacidade de restauração em caso de falhas.

**Suporte a Múltiplos Idiomas:**
- O aplicativo é localizável para suportar diferentes idiomas e regiões, atendendo a uma base de usuários global.

## Tecnologias Utilizadas
- **Backend: Python**
- **Frontend: Django**
- **Banco de Dados: MySQL**
- **Autenticação e Autorização: JSON Web Tokens (JWT)**
- **Gráficos e Visualizações: Matplotlib**
- **Envio de Alertas: Email ou SMS via bibliotecas Python**
- **Integração com APIs de Terceiros: Previsão do tempo para otimização da energia solar**
- **Controle de Versão: Git e GitHub**
- **Containerização: Docker ( talvez? )**

## Design e Interface de usuário
- [LANDPAGE](https://github.com/ferrariz1n/Solar-Open/tree/main/landpage-solaropen)
- [FIGMA](https://www.figma.com/file/KkfqRYg4qZbWhJrMlsQsxz/SolarOpenApp?type=design&node-id=0%3A1&t=9kGWvlB0hZiTA41J-1)

| Login                                      | Home                                      | Detalhes do painél                                      |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| ![Foto 1](foto1.png) | ![Foto 2](foto2.png) | ![Foto 3](foto3.png) |

## Equipe
- Uryel Navarro
- Igor Ferrari
- Isabela Batalha
- Leonardo Preuss
- Daniel Maciel
