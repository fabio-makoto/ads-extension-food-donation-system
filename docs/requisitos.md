# Requisitos do Sistema

## Requisitos Funcionais

### RF01 - Registrar doação
O sistema deve permitir o cadastro de uma nova doação contendo as seguintes informações:
- Nome do doador;
- Alimento;
- Quantidade;
- Data da doação.

### RF02 - Consultar doações
O sistema deve permitir consultar uma doação pelo ID ou pelo nome do doador.

### RF03 - Editar doação
O sistema deve permitir alterar o alimento e a quantidade de uma doação cadastrada.

### RF04 - Excluir doação
O sistema deve permitir excluir uma doação, solicitando confirmação antes da exclusão.

### RF05 - Visualizar relatório
O sistema deve apresentar informações consolidadas sobre as doações realizadas.

### RF06 - Visualizar informações do sistema
O sistema deve disponibilizar uma tela "Sobre" com informações sobre o projeto.

## Requisitos Não Funcionais

### RNF01 - Usabilidade
O sistema deve possuir uma interface simples e intuitiva.

### RNF02 - Desempenho
O sistema deve realizar operações de cadastro e consulta de forma rápida.

### RNF03 - Armazenamento
Os dados devem ser armazenados localmente utilizando SQLite.

### RNF04 - Manutenção
O código-fonte deve ser organizado em módulos para facilitar sua manutenção.