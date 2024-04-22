import {parse} from 'csv-parse';
import {Parser} from '@json2csv/plainjs';
import fs from 'fs';

console.log('Hello World');;
const cleanData = [];
const cleanestData = [];

fs.readFile('./tax.csv', (err, data) => {
	if (err) {
		throw err;
	}
	// console.log(data);
	parse(data, {columns: true}, (err, records) => {
		records.forEach((record) => {
			const rec = {};
			for (const [key, value] of Object.entries(record)) {
				// console.log(value);
				rec[key.trim()] = value.trim();
			}
			cleanData.push(rec);
		});
		// console.log(cleanData);
		cleanData.forEach((cd) => {
			if (cd['PARCELID'].slice(0,3) != 'R72') return;
			if (cd['LUC'].length !== 3) return;
			if (cd['LUC'][0] !== '5') return;
			const rec = {};
			rec['PARCELID'] = cd['PARCELID'];
			rec['OWNERNAME'] = cd['OWNERNAME1'] + ' ' + cd['OWNERNAME2'];
			rec['NBHD'] = cd['NBHD'];
			rec['LUC'] = cd['LUC'];
			rec['HLF1DELQ'] = parseFloat(cd['HLF1DELQ']);
			rec['ZIP'] = cd['PARCEL LOCATION ZIP'];
			rec['LOCATION'] = cd['PARCELLOCATION'];
			cleanestData.push(rec);
		});

		const opts = {};
		const parser = new Parser(opts);
		const csv = parser.parse(cleanestData);
		fs.writeFile('cleanData.csv', csv, 'utf8', function (err) {
			if (err) {
				console.log('An error occured.');
			} else {
				console.log('File saved!');
			}
		});
	});
});
