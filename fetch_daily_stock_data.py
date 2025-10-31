import pandas as pd
import os

# Output file path
output_file = 'numbers.csv'

# Generate numbers 1 to 10
data = {'Number': list(range(1, 11))}
df = pd.DataFrame(data)

# Save to CSV
df.to_csv(output_file, index=False)
print(f"✅ Successfully saved numbers 1 to 10 in {output_file}")
