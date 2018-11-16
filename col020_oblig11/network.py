class Network():
    def __init__(self,edges):
        self.edges = edges
    def add_edge(self,agent_a,agent_b):
        if agent_a == agent_b:
            print('%i and %i can not be added as a friend of itself.'%(agent_a,agent_b))
            return None
        if agent_a in self.edges:
            if agent_b in self.edges[agent_a]:
                pass
            else:
                self.edges[agent_a].append(agent_b)
        else:
            self.edges.update({agent_a:[agent_b]}) 
        if agent_b in self.edges:
            if agent_a in self.edges[agent_b]:
                pass
            else:
                self.edges[agent_b].append(agent_a)
        else:
            self.edges.update({agent_b:[agent_a]})
    def friends_of(self,agent):
        try:
            return self.edges[agent]
        except:
            print('Could not find agent.')
            return None
    def friends_of_these(self,list_of_agents):
        accumulated_friends_list = []
        for i in list_of_agents:
            for j in self.edges:
                accumulated_friends_list.append(j)
        #under tar jeg bort duplikater og trekker fra listen med agenter med å gjøre om list type til set type.
        #set kan trekkes fra set. IE: set([1,2,3,4])-set([2,3]) = set[1,4]
        #Dette i henhold til valgfrie utvidelser i Oppgave 2.
        return list(set(accumulated_friends_list) - set(list_of_agents)) 

def main():
    asdf = Network({0:[1]})
    asdf.add_edge(1,2)
    asdf.add_edge(2,3)
    asdf.add_edge(0,3)
    asdf.add_edge(3,1)
    asdf.add_edge(3,1)
    asdf.add_edge(3,3)
    asdf.add_edge(3,1)
    asdf.add_edge(3,3)
    asdf.add_edge(99,23)
    asdf.add_edge(99,1)
    asdf.add_edge(3,3)
    asdf.add_edge(3,2)
    print(asdf.friends_of(0))
    print(asdf.friends_of(1))
    print(asdf.friends_of(2))
    print(asdf.friends_of(3))
    print(asdf.friends_of(23))
    print(asdf.friends_of(99))
    listasdf=[0,1]
    print(asdf.friends_of_these(listasdf))

if __name__ == '__main__':
    main()