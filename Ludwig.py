# -*- coding: utf-8 -*-

from ludwig import LudwigModel
import yaml
import logging 

#定义函数
def startjob(csv_file_path = r'C:\Users\57855\Desktop\2%test.csv',#训练文件的路径
             model_file = r'C:\Users\57855\Desktop\2%.yaml',#模型配置文件路径
             test_file = r'C:\Users\57855\Desktop\2%test_data.csv'):#结果输出路径
    #Lugwig教程上的代码
    with open(model_file, encoding='utf-8', mode='r') as file:
        model_definition = yaml.load(file.read())
        print(model_definition)
        ludwig_model = LudwigModel(model_definition)
        train_stats = ludwig_model.train(csv_file_path,
                                        logging_level=logging_DEBUG)
        print(train_stats)
        predictions = ludwig_model.predict(test_file,
                                        logging_level=logging_DEBUG)
        print(predictions)
        ludwig_model.close()

if __name__ == '__main__':
    startjob()
