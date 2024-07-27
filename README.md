### Implantação

Para implantar o projeto na AWS usando o Serverless Framework, siga estas etapas:

. Configure suas credenciais da AWS no GitHub Secrets como `AWS_ACCESS_KEY_ID` e `AWS_SECRET_ACCESS_KEY`.
. Certifique-se de ter o Serverless Framework instalado.

```shell
npm i serverless -g
```

```shell
serverless update
```

```shell
sls deploy
```

variações:

```shell
sls deploy
```

Para remover tudo o que está na aws

```shell
sls remove --stage dev
```

exemplos URLs:
✔ Service deployed to stack hackaton-medicine-service-dev (114s)
endpoints:
  POST - https://e1n06wmh69.execute-api.us-east-1.amazonaws.com/dev/doctor
  POST - https://e1n06wmh69.execute-api.us-east-1.amazonaws.com/dev/paciente
  POST - https://e1n06wmh69.execute-api.us-east-1.amazonaws.com/dev/prontuario
  GET - https://e1n06wmh69.execute-api.us-east-1.amazonaws.com/dev/doctors
  GET - https://e1n06wmh69.execute-api.us-east-1.amazonaws.com/dev/pacientes
  GET - https://e1n06wmh69.execute-api.us-east-1.amazonaws.com/dev/prontuario/paciente/{idPaciente}
  GET - https://e1n06wmh69.execute-api.us-east-1.amazonaws.com/dev/prontuario/paciente/{idPaciente}/medico/{idMedico}


## Team
 - Turma: 3SOAT
 - Grupo: 2

   [André Felipe](andrefelipegodoi@gmail.com)
   
   [Bruna Carlota](brunacarlota@gmail.com)

   [Carlos Tofoli](henrique.tofoli@hotmail.com)

   [Guilherme Oliveira](guilherme.oliveira182@yahoo.com.br)

   [Valdeir Jesus](valdeir_014@hotmail.com)
