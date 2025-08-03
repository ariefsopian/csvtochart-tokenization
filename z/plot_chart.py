import pandas as pd
import matplotlib
# Mengatur backend Matplotlib agar tidak menggunakan GUI
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import uuid
import os

def generate_chart(file_path, title):
    """
    Membuat grafik garis dari file CSV.
    
    Args:
        file_path (str): Jalur ke file CSV.
        title (str): Judul grafik.
        
    Returns:
        str: Nama file gambar yang dihasilkan.
    """
    try:
        df = pd.read_csv(file_path, index_col=0, header=0, parse_dates=True)
        df.columns = df.columns.str.strip()

        fig, ax = plt.subplots(figsize=(15, 8))
        ax.plot(df.index, df['Tokenize'], label='Tokenize', marker='o', color='tab:blue')
        ax.plot(df.index, df['Detokenize'], label='Detokenize', marker='o', color='tab:orange')
        
        formatter = ticker.StrMethodFormatter('{x:,.0f}')
        ax.yaxis.set_major_formatter(formatter)
        
        tokenize_peak_value = df['Tokenize'].max()
        tokenize_peak_date = df['Tokenize'].idxmax()
        detokenize_peak_value = df['Detokenize'].max()
        detokenize_peak_date = df['Detokenize'].idxmax()

        ax.text(tokenize_peak_date, tokenize_peak_value, f'{tokenize_peak_value:,}', 
                 ha='center', va='bottom', fontsize=10, fontweight='bold', color='tab:blue')
        ax.text(detokenize_peak_date, detokenize_peak_value, f'{detokenize_peak_value:,}', 
                 ha='center', va='bottom', fontsize=10, fontweight='bold', color='tab:orange')

        ax.set_title(title, fontsize=16)
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Count', fontsize=12)
        
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.6)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        image_filename = f"chart_{uuid.uuid4()}.png"
        image_path = os.path.join("static", image_filename)
        plt.savefig(image_path)
        plt.close(fig)
        
        return image_filename

    except Exception as e:
        print(f"Terjadi kesalahan saat membuat grafik: {e}")
        raise e