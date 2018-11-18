# До-обучение существующей сети на новых классах изображений

Руководство: https://www.tensorflow.org/hub/tutorials/image_retraining

## Результат для примера из руководства

Скачать дообученную модель можно следующим образом:

    `wget https://github.com/zxqfd555/machine-learning-braindump/raw/master/retrain-image-classifier/example-model/output_graph.pb`
    `wget https://github.com/zxqfd555/machine-learning-braindump/raw/master/retrain-image-classifier/example-model/output_graph.txt`

Затем запустить на произвольном изображении (https://www.tensorflow.org/hub/tutorials/image_retraining, секция "Using the retrained model"):

    `curl -LO https://github.com/tensorflow/tensorflow/raw/master/tensorflow/examples/label_image/label_image.py`
    `python label_image.py \
      --graph=output_graph.pb --labels=output_labels.txt \
      --input_layer=Placeholder \
      --output_layer=final_result \
      --image=<path_to_image>`

В конце обучения, качество, которое вернул retrain.py было около 92 процентов.

## Свой датасет

Берем CIFAR-10 и оставляем из него только картинки с котами и собаками. По ссылке: https://pjreddie.com/projects/cifar-10-dataset-mirror/

    `wget http://pjreddie.com/media/files/cifar.tgz`  
    `tar xzf cifar.tgz`
  
Чтоб это сделать, можно сделать что-то вроде:

    `mkdir cat-vs-dog`
    `mkdir cat-vs-dog/cat`
    `mkdir cat-vs-dog/dog`
    `cp cifar/train/*_cat.png cat-vs-dog/cat/`
    `cp cifar/train/*_dog.png cat-vs-dog/dog/`

Картинки даны в png, чтоб запустить код из туториала без изменений, их пришлось сконвертировать в jpg.

    `cd cats-vs-dogs/cat`
    `mogrify -format jpg *.png`
    `cd ../dog`  
    `mogrify -format jpg *.png`
  
Возможно понадобится установить imagemagick:

    `sudo apt-get install imagemagick`

**Но все это проделывать не нужно**, полученный датасет лежит на гитхабе, и можно его просто скачать:

    `wget https://github.com/zxqfd555/machine-learning-braindump/raw/master/retrain-image-classifier/cats-vs-dogs/dataset.tar.gz`
  
И распаковать:

    `tar -xzf dataset.tar.gz`
  
Аналогично, полученная дообученная модель может быть скачана следующим образом:

    `wget https://github.com/zxqfd555/machine-learning-braindump/raw/master/retrain-image-classifier/cats-vs-dogs/output_graph.pb`
    `wget https://github.com/zxqfd555/machine-learning-braindump/raw/master/retrain-image-classifier/cats-vs-dogs/output_graph.txt`
  
В конце обучения, качество, которое вернул `retrain.py` было около 87 процентов.
