from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

class HibernationSubject:
    def __init__(self):
        self.health = 100
        self.hand_intact = True
        self.is_hibernating = True
        self.cut_with_knife = False

subject = HibernationSubject()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cut_hand', methods=['POST'])
def cut_hand():
    if subject.hand_intact:
        damage = random.randint(30, 60)
        subject.health -= damage
        subject.hand_intact = False
        subject.cut_with_knife = False
        return jsonify({
            'message': f"✂️ Hand amputated! Health -{damage}%",
            'health': subject.health,
            'hand_intact': False,
            'is_hibernating': subject.is_hibernating
        })
    return jsonify({'error': 'Hand already missing!'})

@app.route('/cut_with_knife', methods=['POST'])
def cut_with_knife():
    if subject.hand_intact:
        damage = random.randint(10, 30)
        subject.health -= damage
        subject.hand_intact = True  # Hand appears intact
        subject.cut_with_knife = True  # Hidden fatal wound
        return jsonify({
            'message': f"🔪 Made small incision! Health -{damage}%",
            'health': subject.health,
            'hand_intact': True,
            'is_hibernating': subject.is_hibernating
        })
    return jsonify({'error': 'Cannot cut hand again'})

@app.route('/give_meds', methods=['POST'])
def give_meds():
    heal = random.randint(10, 25)
    subject.health = min(100, subject.health + heal)
    return jsonify({
        'message': f"💉 Health +{heal}%",
        'health': subject.health,
        'is_hibernating': subject.is_hibernating
    })

@app.route('/wake_up', methods=['POST'])
def wake_up():
    subject.is_hibernating = False
    if subject.cut_with_knife:
        subject.health = 0
        subject.hand_intact = False  # Show hand missing after death
        return jsonify({
            'message': "💀 Subject never wakes up! Fatal bleeding from small cut.",
            'health': 0,
            'dead': True,
            'hand_intact': False,
            'is_hibernating': False
        })
    elif not subject.hand_intact:
        return jsonify({
            'message': "🚨 Subject wakes screaming! ❌ Hand missing!",
            'health': subject.health,
            'is_hibernating': False
        })
    return jsonify({
        'message': "😊 Subject wakes normally.",
        'health': subject.health,
        'is_hibernating': False
    })

@app.route('/reset', methods=['POST'])
def reset():
    subject.health = 100
    subject.hand_intact = True
    subject.is_hibernating = True
    subject.cut_with_knife = False
    return jsonify({
        'message': "🔁 Experiment reset",
        'health': 100,
        'hand_intact': True,
        'is_hibernating': True
    })

if __name__ == '__main__':
    app.run(debug=True)