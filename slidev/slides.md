---
theme: default
highlighter: prism
title: Aulas de Engenharia de Dados
---

# Engenharia de Dados

Bem-vindo ao repositório onde compartilho o planejamento e conteúdos das minhas aulas sobre Python e Engenharia de Dados. Aqui, você encontrará materiais didáticos, exemplos de código, e recursos adicionais para aprimorar seu aprendizado nessas áreas.

<!--

-->


---
layout: two-cols
---

## Sobre Mim

<img src="https://avatars.githubusercontent.com/u/14779870?v=4" class="m-40 h-40 rounded shadow" />

::right::

Olá, sou [Wellington Faria](https://www.linkedin.com/in/wellicfaria/), um apaixonado por tecnologia e educação. Atuo como Programador Python e Engenheiro de Dados, com formação em Engenharia da Computação. Além do meu interesse profissional em dados e programação, sou entusiasta de plantas, cachorros e aquarismo.

Minha jornada profissional inclui experiências em empresas de tecnologia e finanças, como a Nubank, onde apliquei minhas habilidades em Python e engenharia de dados para resolver desafios complexos. Essas experiências me proporcionaram um vasto conhecimento, que agora busco compartilhar através destas aulas.

<a href="https://github.com/wellicfaria" target="_blank">
  <uim-github class="text-3xl text-red-400 mx-2"/>
</a>

<a href="https://www.linkedin.com/in/wellicfaria/" target="_blank">
  <uim-linkedin class="text-3xl text-red-400 mx-2"/>
</a>

---

## Como Usar Este Repositório

<span style="font-size: 8px;">

Este repositório contém materiais educativos organizados por tópicos, incluindo slides, códigos de exemplo, e listas de recursos adicionais. A duas opçoes de utilizar, trabalhando localmente com Docker e VSCode ou utilizando o GitHub Codespaces, são formas eficazes de acessar e interagir com o conteúdo do curso. Escolha a que melhor se adapta às suas necessidades e preferências de desenvolvimento.

### Trabalhando Localmente com Docker e VSCode

- Certifique-se de que você tem o [Docker](https://www.docker.com/) instalado em sua máquina. Para instalar, siga as instruções na [documentação do Docker](https://docs.docker.com/get-docker/).
-  **Usando o VSCode Remote Containers:**
  - Abra o Visual Studio Code e instale a extensão "Remote - Containers".
  - Com a extensão instalada, abra o comando `Remote-Containers: Open Folder in Container...` e selecione a pasta do tópico desejado.
  - Isso configurará um container Docker com base nas definições do `devcontainer.json`.
  - Para mais detalhes, consulte a [documentação do VSCode sobre Containers Remotos](https://code.visualstudio.com/docs/remote/containers).

### Utilizando GitHub Codespaces

- **Acesso Direto na Nuvem:**
  - Para aqueles que preferem um ambiente de desenvolvimento baseado na nuvem, oferecemos suporte ao GitHub Codespaces.
  - Com o GitHub Codespaces, você pode desenvolver diretamente no navegador, sem necessidade de configuração local.

- **Iniciando um Codespace:**
  - Navegue até o repositório no GitHub, clique na aba 'Code' e selecione a opção 'Open with Codespaces'.
  - Crie um novo Codespace ou conecte-se a um existente para começar a trabalhar.
  - O ambiente de desenvolvimento, incluindo todas as dependências necessárias, será automaticamente configurado para você.
  - **Mais Informações:**
  - Para saber mais sobre como utilizar o GitHub Codespaces, visite a [documentação do GitHub Codespaces](https://docs.github.com/en/codespaces).

</span>

---

## Ambiente Dev Container: Ubuntu-To-Classes


<span style="font-size: 10px;">
Na tabela abaixo, você pode navegar pelas configurações do ambiente de desenvolvimento. O ambiente de desenvolvimento é baseado em um Dev Container do Visual Studio Code, que pode ser executado localmente com Docker ou na nuvem com o GitHub Codespaces.
</span>

### Recursos e Ferramentas

<span style="font-size: 8px;">

| Componente         | Descrição                                                                 | Configurações Adicionais                                       |
| ------------------ | ------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Ubuntu** | Sistema Operacional Ubuntu. | Versão: 21.10  <br> Image: mcr.microsoft.com/devcontainers/base:jammy| 
| **AWS CLI**        | Interface de Linha de Comando da Amazon Web Services.                    | Versão: latest                                                |
| **Azure CLI**      | Interface de Linha de Comando do Microsoft Azure.                        | Versão: latest <br> Instalado via Python: Sim                 |
| **GitHub CLI**     | Interface de Linha de Comando do GitHub.                                 | Versão: latest <br> Instalado diretamente do GitHub Release: Sim |
| **Java**           | Ambiente de desenvolvimento Java, incluindo JDK.                         | Versão: 11                                                    |
| **Python**         | Ambiente de desenvolvimento Python.                                      | Versão: 3.10 <br> JupyterLab: Sim|
| **Docker-in-Docker**| Permite rodar Docker dentro do container do Dev Container.               | Versão: latest                                                |

</span>

---

## Contribuições

<span style="font-size: 10px;">

Contribuições são sempre bem-vindas no projeto [Classes](https://github.com/wellicfaria/classes)! Se você tem sugestões de melhorias, correções de bugs ou novas funcionalidades, aqui está como você pode contribuir:

### Relatando Bugs e Sugerindo Melhorias
- **Abra uma Issue:** Se você encontrou um bug ou tem uma sugestão de melhoria, [abra uma issue](https://github.com/wellicfaria/classes/issues) no GitHub. Certifique-se de descrever claramente o bug ou a sugestão e fornecer todas as informações necessárias para reproduzi-lo ou entender a sugestão.

### Enviando Pull Requests

- **Fork o Repositório:** Primeiro, faça um "fork" do repositório em sua conta do GitHub.
- **Clone o Fork:** Clone o fork para seu ambiente de desenvolvimento local.
- **Crie uma Branch:** Para novas funcionalidades ou correções, crie uma branch a partir da `main`. Dê um nome descritivo para sua branch, como `feature/nome-da-nova-funcionalidade` ou `fix/descrição-do-bug`.
- **Faça suas Alterações:** Implemente suas mudanças em sua branch local. Lembre-se de manter o código limpo e seguir as diretrizes de codificação do projeto, se houver.
- **Teste suas Alterações:** Antes de enviar o pull request, teste suas mudanças para garantir que elas funcionem conforme esperado e não quebrem funcionalidades existentes.
- **Envie o Pull Request:** Após testar suas mudanças, [envie um pull request](https://github.com/wellicfaria/classes/pulls) para a branch `main` do repositório original. No pull request, inclua uma descrição clara das mudanças e qualquer outra informação relevante.


### Diretrizes Gerais

- **Documente seu Código:** Certifique-se de que todas as mudanças ou adições estejam bem documentadas, para que outros colaboradores possam entender e manter seu código no futuro.
- **Respeite o Estilo de Código:** Se o projeto tiver um estilo de código específico ou diretrizes de contribuição, siga-os para manter a consistência.
- **Seja Respeitoso:** Lembre-se de que a contribuição para projetos de código aberto é sobre colaboração. Seja respeitoso e construtivo em suas interações com outros colaboradores.

Agradecemos seu interesse em contribuir para o projeto [Classes](https://github.com/wellicfaria/classes) e estamos ansiosos para ver suas ideias e melhorias!

</span>


---

## Contato

Se você tiver dúvidas ou quiser entrar em contato comigo, pode me enviar um e-mail para [wellicfaria@gmail.com](mailto:wellicfaria@gmail.com).

---

## Agradecimentos

Obrigado por visitar este repositório e espero que os materiais aqui disponibilizados ajudem em sua jornada de aprendizado!

---
src: ./pages/Arquitetura de Data Pipelines/0 - Data Pipelines.md
---




