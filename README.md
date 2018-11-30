# Machine Learning braindump

Всякое-разное про машинное обучение в не особо структурированном виде. Владелец репозитория никому ничего не гарантирует и никакой ответственности за последствия от использования информации отсюда не несет.

# Оглавление
- [До-обучение существующей сверточной нейронной сети на новых классах изображений](#nn-retrain)
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
  - [SqueezeNet: AlexNet-Level Accuracy With 50x Fewer Parameters and <0.5 Mb Model Size](#a2-1)
  - [Densely Connected Convolutional Networks](#a2-2)
  - [Deep Residual Learning for Image Recognition](#a2-3)
  - [Highway and Residual Networks learn Unrolled Iterative Estimation](#a2-4)
  - [Residual Connections Encourage Iterative Inference](#a2-5)
  - [DeCAF: A Deep Convolutional Activation Feature for Generic Visual Recognition](#a2-6)
  - [Very Deep Convolutional Networks for Large-Scale Image Recognition](#a2-7)
  - [Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning](#a2-8)
  - [Geoffrey Hinton on what's wrong with CNNs](#a2-9)

# До-обучение существующей сверточной нейронной сети на новых классах изображений <a name="nn-retrain"></a>

Описано в этом же репозитории, [здесь](https://github.com/zxqfd555/machine-learning-braindump/tree/master/retrain-image-classifier).

# Обзоры статей <a name="articles-overview"></a>

## Introduction to Semi-Supervised Learning with Ladder Networks <a name="a1-1"></a>

Ссылка на статью: https://arxiv.org/abs/1507.02672

Ссылка на блог про статью: http://rinuboney.github.io/2016/01/19/ladder-network.html

Авторами приводится архитектура нейронной сети для смешения концепций обучения с учителем (supervised learning) и без учителя (unsupervised learning). Архитектуру назвали ladder network, так как похожа на лестницу, а способ обучения - semi-supervised learning.

Предполагается, что мы располагаем каким-то небольшим количеством размеченных примеров для обучения с учителем, и некоторым количеством неразмеченных примеров для обучения без учителя. Неразмеченные примеры дешевы и просты в получении поэтому это хорошо, если за счет них можно сократить необходимое количество размеченных примеров.

План по построению архитектуры сети примерно такой:

  1. Создается encoder, который бывает двух типов. Первый добавляет гауссов шум на всех своих слоях, второй - не добавляет никогда.
  
  2. Создается decoder, цель которого - восстанавливать испорченные шумом активации. Штраф decoder'a - разница между тем что получилось, и изначальным, "чистым" объектом.
  
  3. Для оценки качества считается сумма supervised loss - считается с помощью encoder-a с шумом и ответов на оригинальных объектах и unsupervised loss - сумма произведений штрафов на слоях decoder-а на гиперпараметр, который задает значимость этого слоя.
  
  4. Это все тренеруется стандартными методами такими, как стохастический градиентный спуск.
  
Авторам удалось достичь ошибки в 1.06% на MNIST-е, использовав в обучении только 100 размеченных примеров.

## Intro to optimization in deep learning: Busting the myth about batch normalization <a name="a1-2"></a>

Ссылка на статью: https://blog.paperspace.com/busting-the-myths-about-batch-normalization/

Основная идея: мы не понимаем, почему batchnorm делает результаты лучше. С одной стороны его добавление действительно улучшает результаты многих сетей. Но с другой, параметры batchnorm-слоя также меняются в процессе обучения сети и влияют на то, что выдает функция активации, следовательно, постоянно меняют ее распределение. То есть, вызывают тот же Internal Covariate Shift.

Почему он все же делает лучше: есть версия, что контролировать два параметра в batchnorm-слое проще, чем сотни без него - а именно, все веса предыдущего слоя. Это должно ускорять сходимость.

Когда вставлять batchnorm-слой: до активации или после. В оригинальной статье про batchnorm, авторами советовалось вставлять этот слой до активации. Однако авторы этой статьи утверждают, что на практике его лучше вставлять после, так как в этом случае batchnorm сможет более полно контролировать распределение входа на следующий слой. А в случае со вставкой до, выйдет что выход batchnorm-а еще должен будет пройти функцию активации, а только потом отправится на следующий слой. Это может испортить сделанной batchnorm-ом распределение.

## Layer Normalization <a name="a1-3"></a>

Ссылка на статью: https://arxiv.org/abs/1607.06450

Ссылка на блог про сравнение с batch normalization: http://mlexplained.com/2018/01/13/weight-normalization-and-layer-normalization-explained-normalization-in-deep-learning-part-2/

Авторы приводят еще один алгоритм нормализации для ускорения сходимости сети, как альтернативу batch-нормализации. Главное отличие от batchnorm: средние и дисперсии считаются отдельно по каждой из фичей.

Сравнение side-by-side можно найти, например, в блоге про сравнение с batchnorm. Внешне они очень похожи. Авторы статьи в своей статье отмечают, что layernorm лучше подходит для рекуррентный нейронных сетей.

## Deep learning with Elastic Averaging SGD <a name="a1-4"></a>

Ссылка на статью: https://arxiv.org/abs/1412.6651

В статье предлагается новый алгоритм для реализации метода стохастического градиентного спуска - Elastic Averaging SGD или просто EASGD. Он может быть полезен для того, чтобы распараллелить стохастический градиентный спуск. Алгоритм использует идею master+workers.

Каждый воркер хранит какой-то свой вектор переменных, который оптимизирует. Теперь, вместо оптимизации значения функции потерь предлагается оптимизировать сумму (значение функции потерь на переменных воркера + штраф: произведение некоторого скаляра на **||x-x</sub>c</sub>||**, где **x<sub>c</sub>** - некоторая "центральная" переменная). Эквивалентность этих задач известна как global variable consensus. "Elastic" в названии алгоритма про то, что он действует так, будто какая-то эластичная сила не дает ему сильно отойти от центра.

Воркер хранит в себе датасет, текущие значения своих переменных и последнее значение центральной переменной **x<sub>c</sub>**, которое ему сообщили. Воркер делает итерации стохастического градиентного спуска с поправкой на штраф за отдаление от центра. Мастер периодически собирает значения переменных с воркеров и на основании них обновляет значение центральной переменной. Это значение, так же с некоторой периодичностью, доставляется на воркеров. Периодичность надо выбирать таким образом, чтобы не упереться в пересылку данных.

Согласно экспериментам, проведенным авторами статьи, этот метод показал себя лучше имевшихся тогда аналогов (в частности, DOWNPOUR) и сходился быстрее обычного SGD.

## The Marginal Value of Adaptive Gradient Methods in Machine Learning <a name="a1-5"></a>

Ссылка на оригинал статьи: https://arxiv.org/abs/1705.08292

Основная идея состоит в том, что адаптивные методы градиентного спуска не являеются панацеей. Авторы предлагают конструктивный алгоритм для построения примера из довольно небольшого числа объектов (линейного относительно числа измерений), на котором SGD найдет точное решение, а AdaGrad отнесет все объекты к одному классу.

Также авторами проводятся эксперименты, в которых оптимизатор Adam с параметрами по умолчанию показывает себя хуже остальных методов. Путем настройки параметров авторам удается добиться значительного улучшения качества, таким образом опровергнув общепринятое мнение о том, что этот алгоритм не нуждается в настройке параметров. Также делается вывод о том, что зачастую при более быстром росте качества на обучающей выборке, адаптивные алгоритмы не дают значительного прироста на валидационной и тестовой выборках.

## Self-Normalizing Neural Networks <a name="a1-6"></a>

Ссылка на оригинал статьи: https://arxiv.org/pdf/1706.02515.pdf

Ссылка на блог SNN: https://towardsdatascience.com/selu-make-fnns-great-again-snn-8d61526802a9

В статье предлагается идея самонормализующихся нейронных сетей. Нормализацию предлагается делать не так, как это делается в, например, сетях с использованием batchnorm или layernorm, а сделав такую функцию активации, которая будет выдавать значения, которые будут иметь среднее 0 и дисперсию 1. Кстати, тогда не стоит вопроса, куда втыкать batchnorm или другую нормализацию: до активации или после.

В качестве такой функции активации выступает SELU. SELU является расширением уже известной ранее функции активации ELU (введена в https://arxiv.org/abs/1511.07289) - ее домножили на скаляр &#955;. В appendix-е выводятся &#945;, &#955;, которые нужны для само-нормализации.

Кроме этого, самонормализующейся нейронной сети нужна своя инициализация весов. Они выбираются из гауссова распределения со средним 0 и дисперсией 1/|w|.

Также предлагается свой Dropout для регуляризации. Заменять веса на ноль, как в обычном dropout-е не получится, например потому, что ноль - не минимум. Веса заменяются на предел значения функции активации при значении аргумента стремящемся к -&#x221e;, после чего выполняется описанное преобразование для сохранения среднего и дисперсии.

Авторы показывают успех SNN, в том числе на глубоких архитектурах, но не везде SNN работает сильно хорошо. Например, тут сеть с SELU проигрывает RELU: https://www.hardikp.com/2017/07/24/SELU-vs-RELU/

## The Two Phases of Gradient Descent in Deep Learning <a name="a1-7"></a>

Ссылка на статью: https://medium.com/intuitionmachine/the-peculiar-behavior-of-deep-learning-loss-surfaces-330cb741ec17

Автор проводит обзор нескольких статей с ICLR 2017, касающихся стохастического градиентного спуска.

Первый важный пункт, выделенный автором - похоже, что различные алгоритмы стохастического градиентного спуска, будучи запущенными на одних и тех же данных и одной и той же функции потерь, сойдутся в разных местах оптимизируемой поверхности. Автор ссылается на статью "An Empirical Analysis of Deep Network Loss Surfaces", где производится анализ точек, найденных различными алгоритмами SGD на поверхности функции потерь (loss surface).

Далее автор рассматривает статью "Exploring Loss Function Topology with Cyclic Learning Rate", в которой проведен следующий эксперимент: learning rate монотонно циклично увеличивается и уменьшается со временем. При этом, в какой-то момент точность на тестовой выборке резко падает, но затем быстро возвращается обратно. Авторами делается догадка (с отсылкой к другой статье) о том, что это может быть связано с тем, что SGD при обучении имеет две стадии. Первую авторы называют фазой дрифта (drift phase), в ней алгоритм просто исследует пространство решений. По мере сходимости, SGD переходит в фразу диффузии (diffusion phase), в которой решение начинает меняться хаотично, а сходимость замедляться. Возможно, высокий learning rate в случае фазы диффузии и выбивает нас в зону с большим значением функции потерь.

Также, для обычного SGD рассматриваются два графика: среднее значение весов в зависимости от номера итерации и дисперсия весов в зависимости от номера итерации. Первая фаза характеризуется большим средним и малой дисперсией, а вторая наоборот - меньшим средним и большей дисперсией.

## On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima <a name="a1-8"></a>

Ссылка на статью: https://arxiv.org/pdf/1609.04836.pdf

Авторы экспериментально показывают, что большой размер мини-батча при обучении стохастического градиентного спуска обычно ведет к сходимости в "острых" минимумах - таких, что рядом с ними есть точки и с сильно бОльшими значениями, и из этих минимов легко выпрыгнуть куда-то, где целевая функция принимает сильно более плохие значения. Это, в свою очередь, ведет более плохим результатам, чем если бы алгоритм сходился в "плоских" минимумах.

Авторы также экспериментально показывают, что методы с меньшим размером батча гораздо меньше подвержены сходимости в острых минимумах вместо плоских.

В конце статьи авторы ставят вопрос о возможности доказательства такого поведения стохастического градиентного спуска на больших размерах мини-батча.

## Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour <a name="a1-9"></a>

Ссылка на статью: https://research.fb.com/wp-content/uploads/2017/06/imagenet1kin1h5.pdf

Авторы делятся опытом того, как им удалось обучить SGD на датасете ImageNet с большим размером мини-батча. В частности, им удалось обучиться без потери точности с мини-батчем размера 8192.

Для того, чтобы достичь такого результата, они использовали linear scaling rule и новую технику "прогрева" (warmup) на старте - gradual warmup.

Linear scaling rule формулируется следующим образом: когда размер мини-батча умножается на **k**, learning rate также должен быть умножен на **k**.

Gradual warmup заключается в том, что на первых итерациях алгоритма мы обучаем его с постепенно бОльшим learning rate-ом от итерации к итерации. Затем, как эти первые итерации закончились, используем уже выбранную политику learning rate scheduling-а.

## SqueezeNet: AlexNet-Level Accuracy With 50x Fewer Parameters and <0.5 Mb Model Size <a name="a2-1"></a>

Ссылка на статью: https://arxiv.org/pdf/1602.07360.pdf

Мотивация статьи следующая: при достижении некоторого достаточного уровня точности, возникают уже некоторые другие требования к нейронной сети, нежели дальнейшая выжимка какой-то небольшой точности, которая уже не так важна. Авторы ставят целью разработку сети, которая будет достигать точности AlexNet, и при этом будет меньше параметров и в целом весить мало.

Рассматриваются варианты "сжатия" полученной сети с незначительными потерями.

Авторы используют следующие стратегии: заменить большую часть фильтров 3х3 фильтрами 1х1, так как они имеют в 9 раз меньше параметров; уменьшить число входных каналов для фильтров 3х3. Таким образом, основным блоком для построения сети является Fire-модуль (Fire-module), который из сверточного слоя имеющего только сверточные фильтры 1x1 (Squeeze-слой), которые дальше скармливаются слою, содержащему смесь из сверточных фильтров 3х3 и 1х1 (Expand-слой). На выходе Squeeze-слоя применяется ReLU для активации, также и на выходе Expand-слоя (и, соответственно, всего Fire-модуля).

Сама сеть собой представляет 8 Fire-модулей, между которыми есть: сверточный слой и Max Pooling 2x2 (в начале); Max Pooling 2x2 (после первых трех Fire-модулей); Max Pooling 2x2 (после еще четырех Fire-модулей); Dropout 0.5 и сверточный слой - в конце.

## Densely Connected Convolutional Networks <a name="a2-2"></a>

Ссылка на статью: https://arxiv.org/pdf/1608.06993.pdf

Рассматривается еще один вариант нейронной сети: Densely Connected NN (сильно/плотно связная нейронная сеть). Авторы предлагают следующий подход: будем строить нейронную сеть из Dense-блоков. Dense-блок - это такой блок, в котором каждый слой соединен со всеми последующими в блоке. В пример они приводят такую сеть: Conv -> Dense-блок -> Conv -> Pooling -> Dense-блок -> Conv -> Pooling -> Dense-блок -> Pooling -> Слой предсказания. В каждом Dense-блоке авторы предлагают цепочку из четырех сверточных (Conv) слоев.

В качестве мотивации того, почему это хорошо и лучше чем было есть такой аргумент: в Dense-слоях мы боремся с затуханием градиента тем, что он может прийти по Identity-связи (той, которая из слоя во все последующие) во все слои, что перед ним. А без Dense-связей, ему надо было бы еще пройти назад несколько слоев.

По утверждению авторов, такие сети учатся не сильно медленнее обычных, эксперименты же показывают state-of-the-art результаты по состоянию на январь 2018.

## Deep Residual Learning for Image Recognition <a name="a2-3"></a>

Ссылка на статью: https://arxiv.org/abs/1512.03385

Авторами предлагается архитектура, которую проще учить в случае очень глубоких сетей - RESnet.

Строительным блоком для нее является Residual connection, который представляет собой добавление результатам на выходе слоя (после активации) результатам на его входе. Данная связь называется еще Shortcut connection или Identity connection, так как без нее при входе x мы получаем некоторый результат F(x), а с ней, то есть, добавив к результату на входе значение самого входа - F(x) + x, то есть +Id(x).

Авторами показывается, что сеть, построенная с использованием введенного строительного блока хорошо учится даже в случае очень большой глубины. В частности, на CIFAR-10 они получают 1202-слойную сеть, которая получает ошибку 0.1% на тренировке и 7.93% на тесте. Это, правда, чуть хуже, чем 110-слойный RESnet, который имеет на тесте ошибку 6.43%, но тоже хорошо. Авторы указывают на то, что бОльшая ошибка на тесте скорее всего вызвана переобучением сети, однако экспериментов с регуляризацией в рамках статьи не проводят.

## Highway and Residual Networks learn Unrolled Iterative Estimation <a name="a2-4"></a>

Ссылка на статью: https://arxiv.org/abs/1612.07771

Обсуждение про то, почему RESnet - он описан в предыдущей просмотренной статье работает.

Интересны ссылки на некоторые эксперименты, которые были проделаны с Residual-сетями:
   - Если из 15-слойной VGG-сети, обученной для CIFAR-10 удалить любой слой, то ошибка на CIFAR-10 возрастет до 90%. Но для RESnet картина другая: удаление слоя приведет только к небольшому падению качества. Это объясняется тем, что следующий за удаленным слой может сделать примерно то же самое, причем даже на картинках с незначительным шумом;
   - Слои натренированной сети RESnet-110 (потому что слоев в ней 110) пробовали перемешивать. Ошибка по-немного увеливалась с каждым перемещением слоя, но что интересно - многие переупорядочивания привели только к незначительному падению точности. Это мотивируется тем, что многие слои работают примерно с одними и теми же представлениями.
