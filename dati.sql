PRAGMA foreign_keys = ON;

INSERT INTO Paziente (codice, nome, cognome, data_nascita, indirizzo, telefono) VALUES
('P001', 'Carlo', 'Palermo', '2003-09-24', 'Via Giuseppe Garibaldi, 9', '0327 5017538'),
('P002', 'Matilde', 'Costa', '2001-01-13', 'Via Galvani, 39', '0398 1963448'),
('P003', 'Pietro', 'Sagese', '1968-10-18', 'Via Alcide De Gasperi, 67', '0342 8057122'),
('P004', 'Raffaele', 'Colombo', '1956-03-04', 'Via Calcirelli, 37', '0322 0192612'),
('P005', 'Eva', 'Fanucci', '1992-05-15', 'Via Sacchi, 124', '0398 2526615'),
('P006', 'Gina', 'Marchesi', '1944-10-21', 'Via delle Coste, 82', '0312 5772958');

INSERT INTO Medico (codice, nome, cognome, specializzazione, recapito) VALUES
('M001', 'Dalia', 'Rizzo', 'Neurologia', '0323 3544451'),
('M002', 'Ludovica', 'Manfredi', 'Cardiologia', '0341 9523395'),
('M003', 'Umberto', 'Borghi', 'Endocrinologia', '0358 0533869'),
('M004', 'Massimiliano', 'Rinaldis', 'Ortopedia', '0398 6363959');

INSERT INTO Farmaco (codice, nome, princ_attivo, casa_farm) VALUES
('F001', 'Imigran', 'Sumatriptan', 'GSK'),
('F002', 'Cardioaspirina', 'Acido Acetilsalicilico', 'Bayer'),
('F003', 'Coumadin', 'Warfarin', 'Bristol-Myers'),
('F004', 'Metformina', 'Metformina', 'Merck'),
('F005', 'Eutirox', 'Levotiroxina', 'Merck'),
('F006', 'Voltaren', 'Diclofenac', 'Novartis');

INSERT INTO Visita (id, data, ora, motivo, note, costo, paziente_codice, medico_codice) VALUES
('V001', '2025-01-10', '09:00', 'Controllo cardiaco', 'Pressione alta', 50.00, 'P001', 'M002'),
('V002', '2025-01-15', '10:30', 'Mal di testa ricorrente', 'Possibile emicrania', 60.00, 'P002', 'M001'),
('V003', '2025-02-05', '11:00', 'Controllo cardiaco', 'Aritmia lieve', 50.00, 'P003', 'M002'),
('V004', '2025-02-18', '14:00', 'Cefalea cronica', 'Emicrania con aura', 60.00, 'P003', 'M001'),
('V005', '2025-03-06', '09:30', 'Dolore articolare', 'Artrosi al ginocchio', 55.00, 'P004', 'M004'),
('V006', '2025-03-18', '11:30', 'Controllo glicemia', 'Diabete di tipo 2', 45.00, 'P004', 'M003'),
('V007', '2025-04-19', '10:00', 'Controllo tiroide', 'Ipotiroidismo', 45.00, 'P005', 'M003'),
('V008', '2025-05-10', '15:00', 'Dolore alla schiena', 'Ernia lombare', 55.00, 'P006', 'M004'),
('V009', '2025-05-22', '09:00', 'Controllo cardiaco', 'Colesterolo alto', 50.00, 'P001', 'M002'),
('V010', '2025-06-03', '11:00', 'Controllo glicemia', 'Valori nella norma', 45.00, 'P005', 'M003');

INSERT INTO Prescrizione (id, posologia, durata, visita_id, farmaco_codice) VALUES
('PR001', '1 compressa al giorno', '30 giorni', 'V001', 'F002'),
('PR002', '1 compressa al bisogno', '15 giorni', 'V002', 'F001'),
('PR003', '1 compressa al giorno', '60 giorni', 'V003', 'F003'),
('PR004', '1 compressa al bisogno', '20 giorni', 'V004', 'F001'),
('PR005', '1 gel applicazione locale 2x giorno', '20 giorni', 'V005', 'F006'),
('PR006', '1 compressa 2x giorno', '90 giorni', 'V006', 'F004'),
('PR007', '1 compressa al giorno', '180 giorni', 'V007', 'F005'),
('PR008', '1 compressa al giorno', '30 giorni', 'V009', 'F002');
