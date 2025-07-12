function newTaskListener() {
	let input = $("#new-task-input");

	input.on('keypress', (e) => {
		if (e.key === "Enter") {
			let lastTask = $(".tasks .task:not(.new-task)").last()
			let csrf = $("input[name='csrfmiddlewaretoken']").val()

			const formData = new FormData()
			formData.append("csrfmiddlewaretoken", csrf)
			formData.append("task", input.val())

			$.ajax({
				url : "",
			    type: "POST",
				processData: false,
			    contentType: false,
				data: formData,
				success: (data) => {
					let taskHTML = `
						<div class="task" data-id="${data.id}">
			                <div class="task-icon">
			                    <i class="fa fa-check"></i>
			                </div>
							<span class="task-text">${input.val()}</span>
		                </div>
					`

					if (lastTask.length) lastTask.after(taskHTML)
					else $(".tasks").append(taskHTML)
					input.val('')

					let tasks = $(".task:not(.new-task)");
					tasks.off('click');
					taskDoneListener();
				}
			})
		}
	})
}

function taskDoneListener() {
	let tasks = $(".task:not(.new-task)");

	tasks.on('click', (event) => {
		let csrf = $("input[name='csrfmiddlewaretoken']").val()
		let task = $(event.currentTarget);
		let checked = Boolean(task.data("checked"))

		if (!checked) {
			$(task.find(".task-icon")).addClass("checked")
			strikethroughTask(task)
		}
		else {
			$(task.find(".task-icon")).removeClass("checked")
			unStrikethroughTask(task)
		}

		task.data("checked", !checked)

		$.ajax({
			url : "",
		    type: "PUT",
			data: {
				checked: Number(!checked),
				id: task.data('id')
			},
			headers: {
				"X-CSRFToken": csrf
			}
		})
	})
}

/**
 * @param task {jQuery}
 */
function strikethroughTask(task) {
	const text = task.find('.task-text')

	const lineHeight = parseInt(text.css('line-height'));
	const lines = getLineDimensions(text[0])
    const linesCount = lines.length;

	let lineElems = []

    for (let i = 0; i < linesCount; i++) {
        const line = $('<div class="strike-line"></div>');
        line.css({
            'top': (i * lineHeight) + (lineHeight / 2),
            'width': lines[i].width
        });
        text.append(line);
		lineElems.push(line)
    }

	(async () => {
		for (let line of lineElems) {
			line.addClass("strike");
			await wait(100);
		}
	})()
}

function unStrikethroughTask(task) {
	const lines = task.find('.strike-line');

	(async () => {
		for (let i = lines.length - 1; i >= 0; i--) {
	        let line = $(lines[i]);
			line.removeClass("strike")

			await wait(100)
	    }
		await wait(400)
		lines.remove()
	})()
}

$(() => {
	newTaskListener();
	taskDoneListener();
})