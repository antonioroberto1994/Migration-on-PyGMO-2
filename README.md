# Migration-on-PyGMO-2
A python 3 module which implements ring and chain migration for [PyGMO 2](https://esa.github.io/pagmo2/).
>PyGMO is a scientific library for massively parallel optimization. It is built around the idea of providing a unified interface to optimization algorithms and to optimization problems and to make their deployment in massively parallel environments easy.

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
