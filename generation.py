from random import shuffle


class Generation:
    '''
    A whole host of scheduling solutions
    '''

    def __init__(self, solutions, run_options):
        self.solutions = solutions
        self.num_solutions = run_options.num_solutions
        self.pct_elite = run_options.pct_elite
        self.pct_cross = run_options.pct_cross
        self.pct_mut = run_options.pct_mut

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def fitness_list(self):
        return list(map(lambda x: x.get_fitness(), self.solutions))

    def sort_solutions_fitness(self):
        self.solutions = sorted(self.solutions, reverse=True)

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

    def crossover_solutions(self, base_gen):
        num_remaining_solutions = self.num_solutions - len(self.solutions)
        possible_solutions = base_gen.get_crossovers()
        # TODO change this from just taking a shuffled set of the possible solutions and adding
        for _ in range(num_remaining_solutions):
            shuffle(possible_solutions)
            self.solutions.append(possible_solutions[0])
        return None

    def mutate_solutions(self):
        possible_solutions = self.solutions
        shuffle(possible_solutions)
        num_to_mutate = int(self.num_solutions * self.pct_mut)
        for index in range(num_to_mutate):
            possible_solutions[index].mutate()
        return

    def get_elites(self):
        self.sort_solutions_fitness()
        num_of_elites = int(len(self.solutions)*self.pct_elite)
        return self.solutions[:num_of_elites]

    def get_crossovers(self):
        self.sort_solutions_fitness()
        num_of_crossovers = int(len(self.solutions)*self.pct_cross)
        return self.solutions[:num_of_crossovers]
