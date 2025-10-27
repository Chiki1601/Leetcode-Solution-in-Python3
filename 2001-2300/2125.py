class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total_beams = 0
        prev_device_count = 0
        
        # Iterate through each row of the bank
        for row in bank:
            current_device_count = 0
            
            # Count security devices ('1's) in current row
            for cell in row:
                current_device_count += ord(cell) & 1  # Bit trick: '1' & 1 = 1, '0' & 1 = 0
            
            # If current row has devices, calculate beams with previous row
            if current_device_count > 0:
                total_beams += prev_device_count * current_device_count
                prev_device_count = current_device_count
        
        return total_beams
