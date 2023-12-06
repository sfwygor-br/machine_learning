from graphviz import Digraph

# Defina o número de camadas e nós em cada camada
num_layers = 4
nodes_per_layer = [2, 10, 10, 1]  # Número de nós em cada camada

# Inicialize o objeto Digraph
dot = Digraph(format='png', engine='dot')

# Defina atributos globais do grafo
dot.attr(rankdir='LR')
dot.attr(splines='line')

# Defina os nós e arestas do grafo com base nas camadas e nós
for layer in range(num_layers):
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.attr(label=f'layer {layer + 1} ({"Input" if layer == 0 else "Hidden" if layer < num_layers - 1 else "Output"} layer)')
        for node in range(nodes_per_layer[layer]):
            s.node(f'x{layer + 1}_{node + 1}', style='solid', color='blue4' if layer == 0 else 'red2' if layer < num_layers - 1 else 'seagreen2', shape='circle')

    if layer < num_layers - 1:
        for from_node in range(nodes_per_layer[layer]):
            for to_node in range(nodes_per_layer[layer + 1]):
                dot.edge(f'x{layer + 1}_{from_node + 1}', f'a{layer + 2}_{to_node + 1}')

# Salve o arquivo de configuração do Graphviz
dot.render('graphviz_config')
