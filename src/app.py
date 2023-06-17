from flask import Flask, render_template, request, jsonify
import algorithm

app = Flask(__name__)
inversions = None


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def process_data():
        data = request.json
        ordered_images = data.get("orderedImages")
        

        
        ordered_images = list(map(int, ordered_images))

        result = algorithm.rockerPercent(ordered_images)

        
        return jsonify(result=result)
    
if __name__ == '__main__':
    app.run(debug=True)
    
