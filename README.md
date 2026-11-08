# 🚀 Automação e Testes de Infraestrutura: Provisionamento de Servidor Nginx com Ansible, Molecule, Docker e GitHub Actions

Este repositório apresenta uma solução automatizada e robusta de **Infraestrutura como Código (IaC)** para o provisionamento, configuração e teste contínuo de um servidor web **Nginx** em ambiente Linux. O projeto foi desenvolvido com foco em boas práticas de engenharia de confiabilidade, assegurando validações automatizadas de alta precisão em pipelines de Integração Contínua (CI).

---

## 🎯 Proposta e Propósito em Ambientes Corporativos

Em ecossistemas corporativos modernos, a entrega rápida e segura de infraestrutura é um dos pilares da transformação DevOps. A proposta central deste projeto é eliminar o provisionamento manual de servidores — suscetível a erros humanos e desvios de configuração (*configuration drift*) — através de uma abordagem declarativa e auditável.

Os principais propósitos corporativos desta iniciativa incluem:
* **Confiabilidade Garantida por Testes:** Assegurar, de forma automatizada, que o pacote do software foi instalado corretamente, que o serviço está ativo e habilitado no boot, e que as portas de rede necessárias estão abertas e escutando conexões.
* **Idempotência Operacional:** Garantir que a execução repetida da automação altere apenas o que for estritamente necessário, preservando a estabilidade do ambiente produtivo.
* **Padronização e Reprodutibilidade:** Empacotar a lógica de configuração em *Ansible Roles* reutilizáveis e portáveis, permitindo replicação instantânea em qualquer ambiente alvo.

---

## ⚙️ Como o Projeto Opera e Funciona

O fluxo de funcionamento do projeto baseia-se em uma esteira automatizada de validação de infraestrutura estruturada nas seguintes etapas:

1. **Orquestração de Contêineres de Teste:** O framework **Molecule** provisiona um contêiner Docker isolado executando Ubuntu e com suporte nativo ao gerenciador de serviços `systemd`.
2. **Convergência via Ansible:** O playbook de convergência aplica a role desenvolvida no ambiente alvo, atualizando pacotes, instalando o Nginx e configurando seu estado de execução.
3. **Validação de Idempotência:** A automação é executada uma segunda vez para comprovar que nenhuma alteração indesejada é realizada quando o sistema já se encontra no estado desejado.
4. **Auditoria Automatizada (Testinfra):** Um script em Python valida formalmente as asserções de infraestrutura dentro do contêiner.
5. **Integração Contínua (CI):** Todo o ciclo é disparado automaticamente na nuvem através do **GitHub Actions** a cada alteração enviada ao repositório, garantindo que nenhum código defeituoso chegue à branch principal.

---

## 🛠️ Tecnologias Utilizadas

* **[Ansible](https://www.ansible.com/):** Motor de automação declarativa para gerenciamento de configuração e provisionamento de servidores.
* **[Molecule](https://molecule.readthedocs.io/):** Framework de teste para validação de roles do Ansible em ambientes isolados.
* **[Testinfra](https://testinfra.readthedocs.io/):** Biblioteca em Python para escrita de testes de infraestrutura utilizando asserções py.test.
* **[Docker](https://www.docker.com/):** Plataforma de conteinerização utilizada para simular o nó de infraestrutura alvo.
* **[GitHub Actions](https://github.com/features/actions):** Ferramenta de CI/CD para execução automatizada da esteira de testes na nuvem.

---

## 📐 Metodologias Aplicadas

* **Infraestrutura como Código (IaC):** Tratamento de scripts de configuração com o mesmo rigor metodológico do desenvolvimento de software tradicional (versionamento, revisão de código e testes automatizados).
* **Test-Driven Infrastructure (TDI):** Concepção de automações validadas por critérios estritos de aceitação e auditoria automatizada.
* **Integração Contínua (CI):** Validação imediata de mudanças através de pipelines executados em ambientes efêmeros na nuvem.

---

## 💡 Conclusão

Este projeto demonstra a eficácia da união entre o ecossistema Ansible e práticas modernas de teste automatizado de infraestrutura. Ao superar restrições de ambientes locais através de pipelines de CI no GitHub Actions, a solução valida com excelência todo o ciclo de vida de uma role de automação — desde a criação e convergência até a auditoria de pacotes, serviços e portas de rede. O resultado é um modelo altamente escalável, auditável e pronto para ser integrado a esteiras corporativas de missão crítica.

---

**Autor:** Ronaldo Rozendo de Souza  
**Repositório Oficial:** [github.com/Esparta009boy/servidor_nginx](https://github.com/Esparta009boy/servidor_nginx)
