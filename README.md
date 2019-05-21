# Migration-on-PyGMO-2
A python 3 module which implements ring and chain migration for [PyGMO 2](https://esa.github.io/pagmo2/).
>PyGMO is a scientific library for massively parallel optimization. It is built around the idea of providing a unified interface to optimization algorithms and to optimization problems and to make their deployment in massively parallel environments easy.

>Efficient implementantions of bio-inspired and evolutionary algorithms are sided to state-of the art optimization algorithms (Simplex Methods, SQP methods, interior points methods ….) and can be easily mixed (also with your newly invented algorithms) to build a super-algorithm exploiting algoritmic cooperation via the asynchronous, generalized island model.

>Pagmo and pygmo can be used to solve constrained, unconstrained, single objective, multiple objective, continuous and integer optimization problems, stochastic and deterministic problems, as well as to perform research on novel algorithms and paradigms and easily compare them to state of the art implementations of established ones.

## Usage ##
```python
prob = pg.problem(pg.schwefel(2))
algo = pg.algorithm(pg.sade(gen=30))
algo.set_verbosity(10)
archi = pg.archipelago(6, algo=algo, prob=prob, pop_size=4)

print(archi[0].get_population().get_x())
ringMigration(archi,plusOne=True)
print(archi[0].get_population().get_x())
```
