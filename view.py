//
// need these "somethings" change
//

from something import render_to_response

from something import view

def home(request):
	tickers = posts.objects.all()[:20]
	content = {
		'symbol' : 'GME',
		'acc' : '91',
		'vel' : '9',
		'count' : '226',
		'date' : '18/02/2021 06:53:55'
	}
	return render_to_response('index.html', {'posts' : tickers})