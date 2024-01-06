htmlContent = '''
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>Smart Home</title>
		<style>
			* {
				margin: 0;
				padding: 0;
				box-sizing: border-box;
			}
			body {
				background: rgb(25, 25, 25);
				color: rgba(255, 255, 255, 0.9);
			}

			#container {
				width: 100%;
				height: 100%;
				padding: 15px 10px;
				position: relative;
			}
			.center {
				text-align: center;
			}
			.separator {
				width: 100%;
				height: 2px;
				margin: 15px 0;
				background: rgba(255, 255, 255, 0.1);
			}
			.flex-center {
				display: flex;
				align-items: center;
			}
			.flex-center label {
				margin-right: 5px;
			}
			.rangeInput {
				width: 100%;
			}
			.labelWidth {
				width: 50px;
			}
			.flex-col {
				display: flex;
				flex-direction: column;
				gap: 15px 0;
			}
			.customButton {
				outline: none;
				padding: 10px 50px;
				background-color: inherit;
				border: 2px solid mediumslateblue;
				border-radius: 25px;
				color: white;
				font-weight: 700;
				font-size: large;
			}
			.pwmButtons {
				display: flex;
				flex-direction: column;
				width: 75%;
				margin: 0 auto;
				gap: 12px;
			}
		</style>
		<script>
			const getValById = (elementId) => {
				return document.getElementById(elementId).value;
			};

			const pwmSave = () => {
				const red = getValById('pwmRed');
				const green = getValById('pwmGreen');
				const blue = getValById('pwmBlue');
				fetch('/api/pwm', {
					method: 'POST',
					body: JSON.stringify({
						command: 'pwmLed',
						red,
						green,
						blue,
					}),
				});
			};
			const pwmStatus = () => {
				fetch('/api/pwm', {
					method: 'POST',
					body: JSON.stringify({
						command: 'pwmLedStatus',
					}),
				}).then(() => window.location.reload());
			};
		</script>
	</head>
	<body>
		<div id="container">
			<div class="center">
				<h1>Smart Home</h1>
			</div>

			<div class="separator"></div>

			<div class="flex-col">
				<div class="flex-center">
					<label class="labelWidth" for="pwmRed">Red</label>
					<input
						type="range"
						id="pwmRed"
						name="pwmRed"
						min="0"
						max="255"
						value="{pwmRedValue}"
						class="rangeInput"
					/>
				</div>
				<div class="flex-center">
					<label class="labelWidth" for="pwmGreen">Green</label>
					<input
						type="range"
						id="pwmGreen"
						name="pwmGreen"
						min="0"
						max="255"
						value="{pwmGreenValue}"
						class="rangeInput"
					/>
				</div>
				<div class="flex-center">
					<label class="labelWidth" for="pwmBlue">Blue</label>
					<input
						type="range"
						id="pwmBlue"
						name="pwmBlue"
						min="0"
						max="255"
						value="{pwmBlueValue}"
						class="rangeInput"
					/>
				</div>
				<div class="pwmButtons">
					<button class="customButton" onclick="pwmSave()">Save</button>
					<button class="customButton" onclick="pwmStatus()">
						{pwmStatus}
					</button>
				</div>
			</div>

			<div class="separator"></div>
		</div>
	</body>
</html>
'''
