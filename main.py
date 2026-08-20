from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/post')
def post_page():
    return render_template('post.html')

@app.route('/post2')
def post2_page():
    return render_template('post2.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/test', methods=['GET', 'POST']) 
def test():
    return render_template('test.html')      

@app.route('/dist')
def dist():
    return render_template('dist.html')

@app.route('/calc', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        input_value = request.form.get('input_value', type=int)
        
        if input_value is not None and input_value >= 0:
            binary = bin(input_value)[2:]
            
            bit_count = len(binary)
            byte_count = (bit_count + 7) // 8  
            
            binary_padded = binary.zfill(byte_count * 8)
            
            bytes_list = [binary_padded[i:i+8] for i in range(0, len(binary_padded), 8)]
            
            result = {
                'decimal': input_value,
                'binary': binary_padded,
                'bits': binary_padded,
                'bit_count': bit_count,
                'byte_count': byte_count,
                'binary_bytes': ' '.join(bytes_list)
            }
        else:
            result = {
                'error': 'Введите положительное число'
            }
    
    return render_template('calc.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)