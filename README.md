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

Ссылка на статью: https://arxiv.org/abs/1412.6651

В статье предлагается новый алгоритм для реализации метода стохастического градиентного спуска - Elastic Averaging SGD или просто EASGD. Он может быть полезен для того, чтобы распараллелить стохастический градиентный спуск. Алгоритм использует идею master+workers.

Каждый воркер хранит какой-то свой вектор переменных, который оптимизирует. Теперь, вместо оптимизации значения функции потерь предлагается оптимизировать сумму (значение функции потерь на переменных воркера + штраф: произведение некоторого скаляра на **||x-x</sub>c</sub>||**, где **x<sub>c</sub>** - некоторая "центральная" переменная). Эквивалентность этих задач известна как global variable consensus. "Elastic" в названии алгоритма про то, что он действует так, будто какая-то эластичная сила не дает ему сильно отойти от центра.

Воркер хранит в себе датасет, текущие значения своих переменных и последнее значение центральной переменной **x<sub>c</sub>**, которое ему сообщили. Воркер делает итерации стохастического градиентного спуска с поправкой на штраф за отдаление от центра. Мастер периодически собирает значения переменных с воркеров и на основании них обновляет значение центральной переменной. Это значение, так же с некоторой периодичностью, доставляется на воркеров. Периодичность надо выбирать таким образом, чтобы не упереться в пересылку данных.

Согласно экспериментам, проведенным авторами статьи, этот метод показал себя лучше имевшихся тогда аналогов (в частности, DOWNPOUR) и сходился быстрее обычного SGD.

## The Marginal Value of Adaptive Gradient Methods in Machine Learning <a name="a1-5"></a>

## Self-Normalizing Neural Networks <a name="a1-6"></a>

Ссылка на оригинал статьи: https://arxiv.org/pdf/1706.02515.pdf

Ссылка на блог SNN: https://towardsdatascience.com/selu-make-fnns-great-again-snn-8d61526802a9

В статье предлагается идея самонормализующихся нейронных сетей. Нормализацию предлагается делать не так, как это делается в, например, сетях с использованием batchnorm или layernorm, а сделав такую функцию активации, которая будет выдавать значения, которые будут иметь среднее 0 и дисперсию 1. Кстати, тогда не стоит вопроса, куда втыкать batchnorm или другую нормализацию: до активации или после.

В качестве такой функции активации выступает SELU. SELU является расширением уже известной ранее функции активации ELU (введена в https://arxiv.org/abs/1511.07289) - ее домножили на скаляр &#955;. В appendix-е выводятся &#945;, &#955;, которые нужны для само-нормализации.

Кроме этого, самонормализующейся нейронной сети нужна своя инициализация весов. Они выбираются из гауссова распределения со средним 0 и дисперсией 1/|w|.

Также предлагается свой Dropout для регуляризации. Заменять веса на ноль, как в обычном dropout-е не получится, например потому, что ноль - не минимум. Веса заменяются на предел значения функции активации при значении аргумента стремящемся к -&#x221e;, после чего выполняется описанное преобразование для сохранения среднего и дисперсии.

Авторы показывают успех SNN, в том числе на глубоких архитектурах, но не везде SNN работает сильно хорошо. Например, тут сеть с SELU проигрывает RELU: https://www.hardikp.com/2017/07/24/SELU-vs-RELU/

## The Two Phases of Gradient Descent in Deep Learning <a name="a1-7"></a>

## On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima <a name="a1-8"></a>

## Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour <a name="a1-9"></a>
