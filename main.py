from text_to_csv import Splitter
from modelling import LdaModeling


def main():

    if __name__ == '__main__':
        s = Splitter()
        lda_instance = LdaModeling('spark_check.csv')
        gensim_corpus, gensim_dictionary = lda_instance.preprocessing()
        print("gensim_corpus", type(gensim_corpus))
        lda_model = lda_instance.modeling(gensim_corpus = gensim_corpus,gensim_dictionary = gensim_dictionary)
        lda_instance.performance(lda_model = lda_model, gensim_corpus = gensim_corpus, gensim_dictionary= gensim_dictionary)
        lda_plot = lda_instance.plotting(lda_model = lda_model, gensim_corpus = gensim_corpus, gensim_dictionary= gensim_dictionary)
        print("lda_plot" , lda_plot)

main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
