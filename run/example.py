from SSSS.base import SSSS

topic = 'machine learning control'

sub_keyword_list1 = ['machine learning',
                     'reinforcement learning',
                     'deep learning',
                     'neural network',
                     'intelligent',
                     'genetic algorithm',
                     'self-tuning',
                     'self-learning',
                     'advanced']
sub_keyword_list2 = ['control',
                     'daylight control',
                     'windows control',
                     'MPC','Model Predictive Control',
                     'PID control']
sub_keyword_list3 = ['in buildings',
                     'HVAC',
                     'building system']
sub_keyword_list = [sub_keyword_list1, sub_keyword_list2, sub_keyword_list3]

year_from = 2010

year_to = 2020

citation_threshold = 5

number_of_searches_per_key_word_per_year = 10

sleep_interval = 360

SSSS(topic, sub_keyword_list, year_from, year_to, citation_threshold, number_of_searches_per_key_word_per_year, sleep_interval)
