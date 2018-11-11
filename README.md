# Machine Learning braindump

Всякое-разное про машинное обучение в не особо структурированном виде. Владелец репозитория никому ничего не гарантирует и никакой ответственности за последствия от использования информации отсюда не несет.

# Оглавление
- [Обзоры статей](#articles-overview)
  - [Introduction to Semi-Supervised Learning with Ladder Networks](#a1-1)
  - [Intro to optimization in deep learning: Busting the myth about batch normalization](#a1-2)
  - [Layer Normalization](#a1-3)
  - [Deep learning with Elastic Averaging SGD](#a1-4)
  - [The Marginal Value of Adaptive Gradient Methods in Machine Learning](#a1-5)
  - [Self-Normalizing Neural Networks](#a1-6)
  - [The Two Phases of Gradient Descent in Deep Learning](#a1-7)
  - [On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima](#a1-8)
  - [Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour](#a1-9)

# Обзоры статей <a name="articles-overview"></a>

## Introduction to Semi-Supervised Learning with Ladder Networks <a name="a1-1"></a>

## Intro to optimization in deep learning: Busting the myth about batch normalization <a name="a1-2"></a>

## Layer Normalization <a name="a1-3"></a>

## Deep learning with Elastic Averaging SGD <a name="a1-4"></a>

## The Marginal Value of Adaptive Gradient Methods in Machine Learning <a name="a1-5"></a>

## Self-Normalizing Neural Networks <a name="a1-6"></a>

Ссылка на оригинал статьи: https://arxiv.org/pdf/1706.02515.pdf

Ссылка на блог SNN: https://towardsdatascience.com/selu-make-fnns-great-again-snn-8d61526802a9

В статье предлагается идея самонормализующихся нейронных сетей. Нормализацию предлагается делать не так, как это делается в, например, сетях с использованием batchnorm или layernorm, а сделав такую функцию активации, которая будет выдавать значения, которые будут иметь среднее 0 и дисперсию 1. Кстати, тогда не стоит вопроса, куда втыкать batchnorm или другую нормализацию: до активации или после.

В качестве такой функции активации выступает SELU. SELU является расширением уже известной ранее функции активации ELU (введена в https://arxiv.org/abs/1511.07289) - ее домножили на скаляр $\lambda$. В appendix-е выводятся $\alpha, \lambda$, которые нужны для само-нормализации.

Кроме этого, самонормализующейся нейронной сети нужна своя инициализация весов. Они выбираются из гауссова распределения со средним 0 и дисперсией $\frac{1}{|w|}$.

Также предлагается свой Dropout для регуляризации. Заменять веса на ноль, как в обычном dropout-е не получится, например потому, что ноль - не минимум. Веса заменяются на предел значения функции активации при значении аргумента стремящемся к $-\infty$, после чего выполняется описанное преобразование для сохранения среднего и дисперсии.

Авторы показывают успех SNN, в том числе на глубоких архитектурах, но не везде SNN работает сильно хорошо. Например, тут сеть с SELU проигрывает RELU: https://www.hardikp.com/2017/07/24/SELU-vs-RELU/

## The Two Phases of Gradient Descent in Deep Learning <a name="a1-7"></a>

## On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima <a name="a1-8"></a>

## Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour <a name="a1-9"></a>
