function toggleBar(){
	let bar = document.querySelector('.navigation ul');
	let head = document.querySelector('.header .header_content h4');
	//let blockqoute = document.querySelector('.header .header_content center blockqoute');
	if (bar.style.display === 'flex') {
		bar.style.display = 'none';
		head.style.display = 'grid';
		//blockqoute.style.display = 'none';
		
	}else{
		bar.style.display = 'flex';
		head.style.display = 'none';
		//blockqoute.style.display = 'none';

	}
}
function bars(bar) {
	bar.classList.toggle('&#9747');
}

let calcScrollValue = () => {
	let scrollProgress = document.getElementById('progress');
	let progressValue = document.getElementById('progress-value');
	let position = document.documentElement.scrollTop;
	let calcHeight = document.documentElement.scrollHeight -
					document.documentElement.clientHeight;
	let scrollValue = Math.round((position * 100) / calcHeight);
	if (position > 100) {
		scrollProgress.style.display = 'grid';

			}
	else{
		scrollProgress.style.display = 'none';
	};
	scrollProgress.addEventListener("click", () =>{
		document.documentElement.scrollTop = 0;
	});
	scrollProgress.style.background = `conic-gradient(#000 ${scrollValue}%, #fff ${scrollValue}%)`;
};

window.onscroll = calcScrollValue;
window.onload = calcScrollValue;

