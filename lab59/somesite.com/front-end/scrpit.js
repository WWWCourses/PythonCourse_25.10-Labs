const main= document.querySelector('main')

let data = [
	{
		'title': 'Task1',
		'description': 'Some description'
	},
	{
		'title': 'Task2',
		'description': 'Some description'
	},
	{
		'title': 'Task3',
		'description': 'Some description'
	},
	{
		'title': 'Task4',
		'description': 'Some description'
	}
]

let content = ''
data.forEach((item)=>{
	content+=`<div class="news"><span>${item.title}</span>: <span>${item.description}</span>	</div>`
})

main.innerHTML =content

