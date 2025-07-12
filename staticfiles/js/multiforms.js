let step = 1;

function nextStep() {
	if (step < totalSteps) {
		let prevStep = step++;
		let stepToHide = $(`.form-steps .step:nth-child(${prevStep})`);
		let stepToShow = $(`.form-steps .step:nth-child(${step})`);

		stepToHide.fadeOut(200)
		setTimeout(() => {
			stepToShow.fadeIn(200)
		}, 200)
	}
}

function prevStep() {
	if (step > 1) {
		let prevStep = step--;
		let stepToHide = $(`.form-steps .step:nth-child(${prevStep})`);
		let stepToShow = $(`.form-steps .step:nth-child(${step})`);

		stepToHide.fadeOut(200)
		setTimeout(() => {
			stepToShow.fadeIn(200)
		}, 200)
	} else location.href = "/";
}

$(() => {
	$(".auth-form").on("keypress", (event) => {
		if (step !== totalSteps && event.keyCode === 13) {
			event.preventDefault();

			nextStep()
		}
	})
	$(".step-btn.next").on("click", () => nextStep())
	$(".step-btn.prev").on("click", () => prevStep())


	IMask($(".username-input")[0], {mask: /^[a-zA-Z.]+$/})
})