INFO100 Obligatorisk Innlevering 9

Introduksjon

Installerte MySQL Server på laptop og kjørte all SQL mot den i samme rekkefølge som de fremkommer i svar på oppgaver under.
Oppgave 1)

CREATE DATABASE MittOppgaveRegister;
USE MittOppgaveRegister;

Oppgave 2)
	a)
	CREATE TABLE people (	
							personid INT NOT NULL AUTO_INCREMENT, 
							name VARCHAR(255), 
							department VARCHAR(255),
							PRIMARY KEY(personid)
						);
	b)
	CREATE TABLE questions (
							questionid INT NOT NULL  AUTO_INCREMENT, 
							personid INT NOT NULL, 
							question VARCHAR(65535),
							PRIMARY KEY(questionid),
							FOREIGN KEY(personid) REFERENCES people(personid)
							);
	b)
	CREATE TABLE answers (
							answerid INT NOT NULL  AUTO_INCREMENT, 
							questionid INT NOT NULL, 
							personid INT NOT NULL, 
							answer VARCHAR(65535),
							PRIMARY KEY(answerid),
							FOREIGN KEY(questionid) REFERENCES questions(questionid),
							FOREIGN KEY(personid) REFERENCES people(personid)
							);

	SHOW TABLES;
		Result:
			answers
			people
			questions

	DESCRIBE people;
		Result:
			Field		Type			NULL	KEY 	Default		Extra
			personid	int(11)			NO 		PRI 	NULL 		AUTO_INCREMENT
			name		VARCHAR(255)	YES				NULL		
			department	VARCHAR(255)	YES				NULL		

	DESCRIBE questions;
		Result: 
			Field		Type			NULL	KEY 	Default		Extra
			questionid	int(11)			NO 		PRI 	NULL 		AUTO_INCREMENT
			personid 	int(11)			NO 		MUL		NULL		
			question 	VARCHAR(1023)	YES 			NULL 	

	DESCRIBE answers;
		Result: 
			Field		Type			NULL	KEY 	Default		Extra
			answerid	int(11)			NO 		PRI 	NULL 		AUTO_INCREMENT
			questionid	int(11)			NO 		MUL 	NULL 		
			personid 	int(11)			NO 		MUL		NULL		
			answer 		VARCHAR(1023)	YES 			NULL 	
			
Oppgave 3)
	a)
	INSERT INTO people VALUES(NULL,'Ole Olsen', 'IT');
	INSERT INTO people VALUES(NULL,'Nils Nilsen', 'IT');
	INSERT INTO people VALUES(NULL,'Nils Olsen', 'HR');

	INSERT INTO questions VALUES(
									NULL,
									(SELECT personid FROM people WHERE name='Ole Olsen'),
									'Hvor mange tenner har en hval?'
								);
	INSERT INTO questions VALUES(
									NULL,
									(SELECT personid FROM people WHERE name='Ole Olsen'),
									'Hvor mange tenner har en katt?'
								);
	INSERT INTO questions VALUES(
									NULL,
									(SELECT personid FROM people WHERE name='Nils Olsen'),
									'Hvor mange tenner har en hund?'
								);

	INSERT INTO answers VALUES(
									NULL,
									(SELECT questionid FROM questions WHERE question='Hvor mange tenner har en hval?'),
									(SELECT personid FROM people WHERE name='Nils Olsen'),
									'324'
								);


	INSERT INTO answers VALUES(
									NULL,
									(SELECT questionid FROM questions WHERE question='Hvor mange tenner har en hval?'),
									(SELECT personid FROM people WHERE name='Nils Nilsen'),
									'32'
								);


	INSERT INTO answers VALUES(
									NULL,
									(SELECT questionid FROM questions WHERE question='Hvor mange tenner har en katt?'),
									(SELECT personid FROM people WHERE name='Ole Olsen'),
									'Kanskje 51?'
								);
	b)
	SELECT * FROM people;
		Result:
		personid	name		department
		1			NULL		NULL
		2			NULL		NULL
		3			NULL		NULL
		4			NULL		NULL
		5			Ole Olsen	IT
		6			Nils Nilsen	IT
		7			Nils Olsen	HR

		pga syntaxfeil ble det satt inn linjer uten data i people tabellen. I ettertid tenker jeg at name burde være en NOT NULL kolonne.

	c)
	SELECT * FROM questions WHERE personid=7;
		Result:
		questionid 	personid 	question
		3			7			'Hvor mange tenner har en hund?'

	d)
	SELECT questions.question, people.name
	FROM questions, people
	WHERE questions.questionid=1
	AND people.personid=5;
		Result:
		question 							name
		'Hvor mange tenner har en hval?'	Ole Olsen

Oppgave 4)
	a)
	UPDATE people 
	SET name = 'Magne Nilsen' 
	WHERE personid = 6;

	b)
	Pga. min DDL trenger jeg kun å endre navnet i people tabellen. 1 rad.

	c)
	Her vil det også bli et spesielt tilfelle pga DDL. Må slette oppføring for personen i alle tabeller som bruker people sin personid som foreign key.

	DELETE FROM answers WHERE personid=7;
	DELETE FROM questions WHERE personid=7;
	DELETE FROM people WHERE personid=7;

	d)
	Pga. DDL vil jeg ikke få løse ender. Om jeg hadde bygget dette opp uten å bruke foreign keys ville det blitt løse ender.


Oppgave 5)
	a) Ja, denne databasen er normalisert. Navn er lagret en plass, spørsmål er lagret en plass og svar er lagret en plass.
	
	b) 	NOT NULL: I en tuppel i en kolonne med property NOT NULL må det settes inn data ved skriving/endring.
		PRIMARY KEY: Her defineres kolonnen som hovednøkkel som må være unik. Brukes som referanse fra andre tabeller.
		AUTO_INCREMENT: denne teller opp og genererer automatisk nye nøkler/tall for hver ny rad som settes inn.

		





	




