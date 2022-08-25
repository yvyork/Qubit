// Initialize DB 

INSERT INTO ticketing_counter (id, counter_name)
VALUES (1, 'Schalter 1'),
(2, 'Schalter 2'),
(3, 'Schalter 3');

// The Zero-Ticket is always needed to start the counter
// Fix in later version
INSERT INTO ticketing_ticket (id, number, timestamp, wait, called)
VALUES (1, 100, now(), 5, true);