from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Product Manager',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 40,00,000',
    'Comapny': 'Paytm'
  },
  {
    'id': 2,
    'title': 'Senior Product Manager',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 80,00,000',
    'Comapny': 'Amazon'
  },
  {
    'id': 3,
    'title': 'Associate Product Manager',
    'location': 'Delhi, India',
    'salary': 'Rs. 20,00,000',
    'Comapny': 'Flask'
  },
  {
    'id': 4,
    'title': 'Associate Product Manager',
    'location': 'Mumbai, India', 
    'Comapny': 'Navi'
  },
  
]

@app.route('/')
def product_jobs():
  return render_template('home.html', jobs=JOBS)
@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)



  