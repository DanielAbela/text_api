text = '''Financial Services (FS) is a sector that is changing rapidly. Faced with more agile market entrants and ever-evolving customer demands, most FS firms now have innovation teams charged with looking for new ways of working and transforming their business.There is a desire to utilize new and innovative technologies such as data analytics and augmented intelligence\u00a0to deliver value to the organization, but there is also a need to mitigate any risk associated with that, real or perceived. This is how\u00a0Synpulse\u00a0deploying Squirro over\u00a0Amazon Web Services\u00a0(AWS) delivers such value \u2013 it enables a faster pace of innovation and demonstrates that risk is manageable.AWS can allow users to deploy the most state-of-the-art technologies \u2013 such as Squirro \u2013 to experiment and innovate more effectively and at a significantly greater pace\u00a0\u2013 taking it step by step without compromising security risk. In a conservative and heavily regulated sector, it can be difficult to get the wider organization's backing for augmented intelligence projects. Sandbox piloting is needed to overcome the 'chicken-egg' issue where investment is required to actually proof tangible results \u2013 but in return, the resulting proof is the only way to unlock this initial investment. Even if AWS-enabled pilots allowed to take this first hurdle, the endeavor will constantly get questioned and the need to justify further activity is a steady companion.That's why Synpulse has been deploying Squirro over AWS in many POCs (Proof-of-Concepts) with such positive effect \u2013\u00a0delivering fast and agile proof to FS firms all over the world.Squirro and Synpulse have now worked in collaboration for several years. Synpulse has a reputation as one of the most knowledgeable global FS consultancies, working with many of the world's largest FS companies to help them realize their business objectives with banking, insurance or re-insurance expertise, combined with our experience to implement IT applications (from core-systems to specialized solutions, like the NLP analytics platform Squirro).As part of Synpulse's commitment to delivering to its clients the latest digitalization trends, it partners closely and develops practical use-cases based on\u00a0proven success in Artificial Intelligence (AI) and Natural Language Processing (NLP)\u00a0from leading experts in this field, such as Squirro.Our many joint projects for banking and insurance clients around the world have included POCs, implementations, and integration of the Squirro solution within a client's IT landscape, and multiple agile enhancement projects, as Heiko Fischer, Associate Partner and expert for cognitive analytics at Synpulse, explains:\u201cThe combination of Synpulse's management consulting and industry expertise with Squirro's AI and machine learning capabilities has had a significant impact on our joint projects. These projects range from lead sourcing to Know Your Customer (KYC) initiatives, delivering to our FS clients a deep customer insight that is used to transformative effect within the business.\u201dBut\u00a0it's the use of Squirro over AWS that can bring the most agility and speed to client PoC projects. In such a fast-paced business climate FS firms must react more quickly than their competition in order to ensure a competitive edge. Each PoC needs to justify itself with tangible returns to gain C-suite attention, and Squirro over AWS delivers this time after time.AWS offers many extensive services from its worldwide data centers, with more functionality than other cloud providers. This makes it faster and more cost-effective to move existing applications to the cloud and for Synpulse and Squirro means that global PoC instances can be quickly and easily deployed.It's also highly secure. The AWS core infrastructure is designed to meet the requirements for the military, FS companies, and other high-security organizations. Because of this functionality, it means that FS organizations can be assured that AWS-based instances are fully secure and that they can keep any confidential data private.This is all really important for agile PoC ramp-up with FS companies. It means that new servers can be securely established in seconds and the installation of Squirro analytics can be done within minutes, which allows for flexible prototyping and testing, and speedier assessment of results. As Heiko Fischer states:\u201cWhile PoCs can be carried out on-premise, it is much slower and more expensive to do so. Using a bank's internal lab can add months to a PoC, which when speed and agility are so important, makes such a project almost untenable. We do all our PoCs with Squirro over AWS \u2013 it is secure, fast and we have results back and ready for assessment within weeks.\u201dWorking with Squirro over AWS allows FS companies to really see the benefit that comes from\u00a0working with unstructured data. Their own legacy, internal data can be connected with external, unstructured data, such as earnings reports, news alerts, and premium data sources.Doing so allows FS firms to aggregate years of relevant data from multiple data sources which would take far too long if approached manually, while also ensuring that the very latest real-time datasets can be included in analysis to derive meaningful insights. This comprehensive and 360-degree perspective delivers actionable insight that can then be used to demonstrate the value of that PoC and how it might work at a larger scale.\u00a0As Heiko Fischer explains:\u201cPoCs are the perfect way for FS firms to try something new at a low cost and with low risk, test new technologies such as augmented intelligence and make an informed decision as to how they might work across the wider organization. We make up three parts of a compelling proposition for FS firms: Synpulse brings its expertise and know-how of the FS market, Squirro is the power under the hood and AWS is the enabler, allowing PoCs to be fast, agile and used to get further business and opportunities.\u201dWith the competition also innovating, any FS firm not embracing data analysis and augmented intelligence risks being left behind. For further details on how Synpulse and Squirro are using AWS to deliver fast and agile PoCs for FS clients, please get in touch with us\u00a0here.'''
import heapq
from collections import defaultdict

import nltk


class Summary:
    MAXIMUM_SENTENCE_LENGTH = 30

    def __init__(self, text):
        self.text = text

    def _filter_out_stopwords(self):
        return [word for word in self.text if word not in nltk.corpus.stopwords.words('english')]

    def _calculate_word_frequencies(self):
        word_frequencies = defaultdict(int)
        for word in self._filter_out_stopwords():
            word_frequencies[word] += 1
        return word_frequencies

    def _calculate_weighted_word_frequencies(self):
        word_frequencies = self._calculate_word_frequencies()
        weighted_word_frequencies = dict()
        maximum_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            weighted_word_frequencies[word] = word_frequencies[word] / maximum_frequency
        return weighted_word_frequencies

    def _calculate_sentence_scores(self, weighted_word_frequencies, max_sentence_length=MAXIMUM_SENTENCE_LENGTH):
        sentence_scores = defaultdict(int)
        sentences = nltk.sent_tokenize(self.text)
        for sentence in sentences:
            for word in nltk.word_tokenize(sentence.lower()):
                if word in weighted_word_frequencies.keys() and len(sentence.split(' ')) < max_sentence_length:
                    sentence_scores[sentence] += weighted_word_frequencies[word]
        return sentence_scores

    def create(self):
        weighted_word_frequencies = self._calculate_weighted_word_frequencies()
        sentence_scores = self._calculate_sentence_scores(weighted_word_frequencies)
        return heapq.nlargest(7, sentence_scores, key=sentence_scores.get)


# import re
#
# formatted_article_text = re.sub('[^a-zA-Z]', ' ', text)
# formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

print(Summary(text).create())
