0
```mermaid

%%(["это либо старт либо конец"])
%%["прямоугольник, для действий, присваиваний или вычислений"]
%%%{"ромб, для вопросов или условий"}
%%[/"паралелограм, для ввода или вывода"/]

```
```mermaid
flowchart TD

    start([Start]) --> cisla["i = 0
    count = 0
    total = 0"] --> podminka1{"i < len(numbers)?"} -- ano -->prirovnavani1["n = numbers[i]"]
    prirovnavani1 -->podminka2{"n == 1?"} -- ne -->podminka3{"n % 2 == 0?"}
    podminka1 -- ne --> vypis["Vypiš count a total"] -->kn([Konec])
    podminka2 -- ano -->vypis
    podminka3 -- ano -->prirovnavani2["total = total + n
    count = count +1"] -->prirovnavani3["i = i + 1"]
    podminka3 -- ne -->prirovnavani3
    prirovnavani3 --> podminka1


```


```mermaid
    flowchart TD
    start([Start])-->prirovnavani1["N = 5
    total = 0"]-->dej1["Zadej N čísel"]-->porovnavani1{"1<=i<=N"}
    porovnavani1 -- ano -->dej2["Načti x"]-->prirovnavani2["total += x"]-->kn([Konec])
    porovnavani1 -- ne -->



```