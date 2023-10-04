import random

def simulate_queue_events(arrival_rate, departure_rate, buffer_size, num_events):
    # Initialize variables/counters related to the queue status.
    pkt_in_q = 0
    pkt_dropped = 0
    output_file = f"i{arrival_rate}_o{departure_rate}_n{buffer_size}.txt"
    
    with open(output_file, 'w') as file:
        file.write("event_seq, pkt_in_q, pkt_dropped\n")
        
    # Simulating the events
    for event_seq in range(1,num_events+1):
        # Generate random [0, 1)
        y = random.random()

        if y < (arrival_rate / (departure_rate + arrival_rate)):
            # Arrival event
            if pkt_in_q < buffer_size:
                pkt_in_q += 1
            else:
                pkt_dropped += 1
        else:
            # Departure event
            if pkt_in_q > 0:
                pkt_in_q -= 1

        # Write results to the specified output file
        with open(output_file, 'a') as file:
            file.write(f"{event_seq} {pkt_in_q} {pkt_dropped}\n")
    print(f"Simulation completed. Results are written to {output_file}.")

# usage
arrival_rate = 30 # λ
departure_rate = 50 # μ
buffer_size = 50 # n
num_events = 1000000 # x

simulate_queue_events(arrival_rate, departure_rate, buffer_size, num_events)

