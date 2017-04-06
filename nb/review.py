punctuation = ['!','?','~','.',',','\"','@','/','(',')','*','$',"&",'#'];

stop_words = ['i','until', 'wrong', 'checked', 'service', 'shower', 'came', 'than', 'smelled', 'asked', 'much', 'had', 'old', 'people', 'for', 'floor', 'smell', 'time', 'so', 'one', '2', 'say', 'going', 'around', 'her', 'with', 'dirty', 'an', 'as', 'at', 'to', 'small', 'seemed', 'hours', 'more', 'door', 'found', 'person', 'be', 'by', 'into', 'line', 'up', 'us', 'next', 'this', 'could', 'should', 'upon', 'desk', 'told', 'work', 'worst', 'then', 'them', 'they', 'another', 'do', 'we', 'air', 'the', 'night', 'available', 'way', 'was', "didn't", 'cold', 'still', 'not', 'down', 'card', 'price', 'only', 'your', 'that', 'you', 'poor', 'rude', 'a', 'off', 'else', 'while', 'some', 'reservation', 'go', 'front', 'times', 'bed', 'she', 'he', 'even', 'never', 'call', 'room', 'before', 'better', 'went', 'bad', 'said', 'it', 'in', 'if', 'make', 'left', 'just', 'manager', 'finally', 'did', 'clerk', 'wait', 'staying', 'morning', 'after', 'think', 'first', 'long', 'were', 'sheets', 'get', 'pay', 'same', 'money', 'disappointed', "wasn't", 'again', 'two', 'hour', 'someone', 'walls', 'hard', 'find', 'back', 'day', 'have', 'like', 'noise', 'about', 'but', 'minutes', 'would', 'phone', 'me', 'my', 'over', 'got', 'took', '-', 'though', 'however', 'towels', 'bathroom', 'been', 'expected', 'experience', 'gave', 'check', 'no', 'charge', 'water', 'given', 'and', 'any', 'later', 'good', 'when', 'on', 'of', 'or', 'there', 'toilet', 'requested', 'booked', 'all', 'what', "don't", 'hotel', 'cleaned', 'nothing', 'his', 'arrived', 'called', 'once', 'waiting', 'use', 'our', 'out', 'their', 'who', 'looked', 'will', 'know', 'because', 'made', 'other']


class_dict = {
    "truthful positive":"0",
    "deceptive positive":"1",
    "truthful negative":"2",
    "deceptive negative":"3"
}

class Review:

    def __init__(self,text,labels):
        splitstr = text.split(" ");
        self.id = splitstr[0];
        self.sentence = " ".join(splitstr[1:]);
        for punc in punctuation:
            self.sentence = self.sentence.replace(punc, ' ');
        self.tokens = self.sentence.lower().split(" ");
        self.tokens = [i for i in self.tokens if i not in stop_words and i]
        self.keywords = []
        self.label = "";
        if labels:
            self.label = class_dict[" ".join(labels.split(" ")[1:])]

    def get_tokens(self):
        return self.tokens;

    def __str__(self):
        s = ""
        s += "id:" + self.id + "   labels:" + self.label + "  tokens:" + str(self.tokens);
        return s;
