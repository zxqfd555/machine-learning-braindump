# До-обучение существующей сети на новых классах изображений

Руководство: https://www.tensorflow.org/hub/tutorials/image_retraining

## Результат для примера из руководства

Скачать можно следующим образом:

  wget https://github.com/zxqfd555/machine-learning-braindump/raw/master/retrain-image-classifier/example-model/output_graph.pb

  wget https://github.com/zxqfd555/machine-learning-braindump/raw/master/retrain-image-classifier/example-model/output_graph.txt

Затем запустить на произвольном изображении (https://www.tensorflow.org/hub/tutorials/image_retraining, using the retrained model):

  curl -LO https://github.com/tensorflow/tensorflow/raw/master/tensorflow/examples/label_image/label_image.py
  python label_image.py \
  --graph=output_graph.pb --labels=output_labels.txt \
  --input_layer=Placeholder \
  --output_layer=final_result \
  --image=<path_to_image>

## Свой датасет

Берем CIFAR-10 и оставляем из него только картинки с котами и собаками. По ссылке: https://pjreddie.com/projects/cifar-10-dataset-mirror/

  wget http://pjreddie.com/media/files/cifar.tgz
  tar xzf cifar.tgz

Катинки даны в png, чтоб запустить код из туториала без изменений, их пришлось сконвертировать в jpg.


