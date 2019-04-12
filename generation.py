class Generation:
    '''
    A whole host of scheduling solutions
    '''

    def __init__(self, solutions):
        self.solutions = solutions

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def fitness_list(self):
        return list(map(lambda x: x.get_fitness(), self.solutions))

    def min_fitness(self):
        min_fitness = self.solutions[0].get_fitness()
        for solution in self.solutions:
            cur_fitness = solution.get_fitness()
            if cur_fitness < min_fitness:
                min_fitness = cur_fitness
        return min_fitness

    def max_fitness(self):
        max_fitness = self.solutions[0].get_fitness()
        for solution in self.solutions:
            cur_fitness = solution.get_fitness()
            if cur_fitness > max_fitness:
                max_fitness = cur_fitness
        return max_fitness

    def avg_fitness(self):
        total = 0
        for solution in self.solutions:
            total += solution.get_fitness()
        return round(total / len(self.solutions))
