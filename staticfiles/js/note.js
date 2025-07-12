function noteSaveForm() {
	let btn = $("#note-save-button")
	let form = btn[0].form
	let selector = $(".day-mood-selector")
	let moodButtons = $(".day-mood-selector .option")
	let moodDetails = $(".day-mood-selector .details")

	moodButtons.on("click", (event) => {
		moodDetails.css({height: moodDetails.height() + "px"})
		moodDetails.animate({
			height: "0px"
		}, 1200)
		selector.animate({
			gap: "0px"
		}, 1200)


		let button = $(event.currentTarget);
		moodButtons.removeClass("lifted")
		button.addClass("lifted")
		$("#mood-hidden-input").val(
			button.data('mood')
		);
	})

	btn.on('click', (event) => {
		event.preventDefault()

		let note = $(".note-container").text()
		$("#note-hidden-input").val(note);

		if (note.length) form.submit()
	})
}

$(() => {
	noteSaveForm()
})