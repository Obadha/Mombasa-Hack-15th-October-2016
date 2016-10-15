from flask import Flask
from flask import jsonify, make_response
from flask import request

app = Flask ('the-box-library')

books = [{
	 'name': 'Jurassic Park',
	 'author': 'Michael Crichton',
	 'id': '554',
	 'category': 'Thriller'
},
{
	 'name': 'Halo The Fall of Reach',
	 'author': 'Eric Nylund',
	 'id': '574',
	 'category': 'Sci-Fi'
}
]

resp = ''
@app.route('/api/category/books', methods = ['GET','POST'])
def book_api():
	if request.method == 'GET':
		return jsonify(books)
		#resp = jsonify(books)
	else:
		name = request.values.get('name',None)
		author = request.values.get('author',None)
		category = request.values.get('category',None)
		id_ = request.values.get('id',None)

		new_book = {
			'name' : name,
			'author': author,
			'category': category,
			'id':id_
		}

		books.append(new_book)
		return jsonify({'OK':'Book added'})

		#resp = jsonity({'OK':'Book added'})

return resp


	


if __name__ == '__main__':
	app.run()