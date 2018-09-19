import rospy
from chatbot_interface.srv import ChatbotInterface, ChatbotInterfaceResponse
import requests
import json

class AlanaInterface(object):
    def __init__(self):
        rospy.init_node('alana_node')
        rospy.Service('~get_answer', ChatbotInterface, self.callback)

    def callback(self, request):
#        result = self.alana.get_answer(session_id=request.session_id, text=request.question, avg_conf_score=request.confidence_score)
        print "REQUEST: ", request
        try:
           t = json.loads(request.question)
        except ValueError:
           t = request.question

#sorted_hypotheses = [{'confidence': 1.0,
#                              'tokens': t.split(),
#                              'token_conf': len(t.split()) *[1.0],
#                              'pauses': (len(t.split()) - 1) *[0]}]
#        res = requests.post('http://localhost:5005/', json=json.dumps({'text': t, 'session_id':
        res = requests.post('http://35.171.3.183:5000/', json=json.dumps({'question': t, 'session_id':
                                                                       request.session_id,
                                                                       'user_id': request.user_id}))
        print "RESPONSE: ", res.text, type(res.text)
        result = json.loads(res.text)
        return ChatbotInterfaceResponse(response=json.dumps(result.get('result')))


if __name__ == '__main__':
    alana_interface = AlanaInterface()
    rospy.spin()
