"""
MercadoLibre - Resumen Ejecutivo
Datos extraídos del archivo: MercadoLibre-Resumen-ejecutivo.xlsx
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# ─────────────────────────────────────────────
# 1. EMBUDO GENERAL
# ─────────────────────────────────────────────

embudo_general = pd.DataFrame([{
    "conversion_select_item":       76.8974,
    "conversion_add_to_cart":       11.0092,
    "conversion_begin_checkout":     4.0033,
    "conversion_add_shipping_info":  2.4187,
    "conversion_add_payment_info":   2.0851,
    "conversion_purchase":           1.2510,
}])

# ─────────────────────────────────────────────
# 2. EMBUDO POR PAÍS
# ─────────────────────────────────────────────

embudo_pais = pd.DataFrame([
    {"country": "Uruguay",   "conversion_select_item": 81.8182, "conversion_add_to_cart": 22.7273, "conversion_begin_checkout": 4.5455, "conversion_add_shipping_info": 4.5455, "conversion_add_payment_info": 4.5455, "conversion_purchase": 4.5455},
    {"country": "Bolivia",   "conversion_select_item": 80.6452, "conversion_add_to_cart":  9.6774, "conversion_begin_checkout": 3.2258, "conversion_add_shipping_info": 3.2258, "conversion_add_payment_info": 3.2258, "conversion_purchase": 3.2258},
    {"country": "Mexico",    "conversion_select_item": 79.7521, "conversion_add_to_cart": 13.2231, "conversion_begin_checkout": 4.1322, "conversion_add_shipping_info": 3.3058, "conversion_add_payment_info": 2.8926, "conversion_purchase": 2.4793},
    {"country": "Peru",      "conversion_select_item": 84.5455, "conversion_add_to_cart": 10.0000, "conversion_begin_checkout": 2.7273, "conversion_add_shipping_info": 2.7273, "conversion_add_payment_info": 1.8182, "conversion_purchase": 1.8182},
    {"country": "Argentina", "conversion_select_item": 75.0000, "conversion_add_to_cart":  8.7500, "conversion_begin_checkout": 4.3750, "conversion_add_shipping_info": 1.8750, "conversion_add_payment_info": 1.8750, "conversion_purchase": 1.2500},
    {"country": "Chile",     "conversion_select_item": 78.3505, "conversion_add_to_cart": 17.5258, "conversion_begin_checkout": 8.2474, "conversion_add_shipping_info": 3.0928, "conversion_add_payment_info": 2.0619, "conversion_purchase": 1.0309},
    {"country": "Brazil",    "conversion_select_item": 72.6027, "conversion_add_to_cart":  8.9041, "conversion_begin_checkout": 2.3973, "conversion_add_shipping_info": 1.3699, "conversion_add_payment_info": 1.3699, "conversion_purchase": 0.6849},
    {"country": "Ecuador",   "conversion_select_item": 74.5763, "conversion_add_to_cart": 10.1695, "conversion_begin_checkout": 5.0847, "conversion_add_shipping_info": 1.6949, "conversion_add_payment_info": 1.6949, "conversion_purchase": 0.0000},
    {"country": "Colombia",  "conversion_select_item": 76.3636, "conversion_add_to_cart":  9.6970, "conversion_begin_checkout": 4.8485, "conversion_add_shipping_info": 3.0303, "conversion_add_payment_info": 2.4242, "conversion_purchase": 0.0000},
    {"country": "Paraguay",  "conversion_select_item": 71.4286, "conversion_add_to_cart":  9.5238, "conversion_begin_checkout": 0.0000, "conversion_add_shipping_info": 0.0000, "conversion_add_payment_info": 0.0000, "conversion_purchase": 0.0000},
])

# ─────────────────────────────────────────────
# 3. RETENCIÓN POR PAÍS
# ─────────────────────────────────────────────

retencion_pais = pd.DataFrame([
    {"country": "Argentina", "retention_d7_pct": 85.1, "retention_d14_pct": 52.3, "retention_d21_pct": 22.5, "retention_d28_pct": 1.8},
    {"country": "Bolivia",   "retention_d7_pct": 80.8, "retention_d14_pct": 46.8, "retention_d21_pct": 19.2, "retention_d28_pct": 2.5},
    {"country": "Brazil",    "retention_d7_pct": 87.2, "retention_d14_pct": 54.4, "retention_d21_pct": 24.4, "retention_d28_pct": 2.5},
    {"country": "Chile",     "retention_d7_pct": 83.7, "retention_d14_pct": 51.8, "retention_d21_pct": 22.1, "retention_d28_pct": 1.7},
    {"country": "Colombia",  "retention_d7_pct": 84.5, "retention_d14_pct": 52.0, "retention_d21_pct": 21.8, "retention_d28_pct": 1.6},
    {"country": "Ecuador",   "retention_d7_pct": 79.1, "retention_d14_pct": 50.0, "retention_d21_pct": 20.6, "retention_d28_pct": 2.5},
    {"country": "Mexico",    "retention_d7_pct": 86.1, "retention_d14_pct": 55.8, "retention_d21_pct": 25.5, "retention_d28_pct": 3.1},
    {"country": "Paraguay",  "retention_d7_pct": 80.9, "retention_d14_pct": 49.1, "retention_d21_pct": 22.1, "retention_d28_pct": 2.1},
    {"country": "Peru",      "retention_d7_pct": 84.3, "retention_d14_pct": 51.1, "retention_d21_pct": 22.9, "retention_d28_pct": 3.2},
    {"country": "Uruguay",   "retention_d7_pct": 86.1, "retention_d14_pct": 48.8, "retention_d21_pct": 23.0, "retention_d28_pct": 2.5},
])

# ─────────────────────────────────────────────
# 4. RETENCIÓN POR COHORTE
# Fechas reales: cohorte mensual Jan–Aug 2025
# ─────────────────────────────────────────────

retencion_cohort = pd.DataFrame([
    {"cohort": "Ene-2025", "retention_d7_pct": 86.2, "retention_d14_pct": 56.2, "retention_d21_pct": 24.1, "retention_d28_pct": 3.0},
    {"cohort": "Feb-2025", "retention_d7_pct": 86.8, "retention_d14_pct": 56.0, "retention_d21_pct": 24.6, "retention_d28_pct": 2.7},
    {"cohort": "Mar-2025", "retention_d7_pct": 87.7, "retention_d14_pct": 56.8, "retention_d21_pct": 26.6, "retention_d28_pct": 3.0},
    {"cohort": "Abr-2025", "retention_d7_pct": 87.2, "retention_d14_pct": 53.9, "retention_d21_pct": 23.0, "retention_d28_pct": 2.0},
    {"cohort": "May-2025", "retention_d7_pct": 86.0, "retention_d14_pct": 54.5, "retention_d21_pct": 26.2, "retention_d28_pct": 3.0},
    {"cohort": "Jun-2025", "retention_d7_pct": 85.9, "retention_d14_pct": 55.1, "retention_d21_pct": 25.2, "retention_d28_pct": 2.1},
    {"cohort": "Jul-2025", "retention_d7_pct": 86.4, "retention_d14_pct": 56.4, "retention_d21_pct": 25.9, "retention_d28_pct": 2.7},
    {"cohort": "Ago-2025", "retention_d7_pct": 70.8, "retention_d14_pct": 29.7, "retention_d21_pct":  7.5, "retention_d28_pct": 0.2},
])

# ─────────────────────────────────────────────
# HALLAZGOS Y REFLEXIÓN (texto del informe)
# ─────────────────────────────────────────────

hallazgos = {
    "embudo": {
        "hallazgo": (
            "Alta retención inicial pero rápida caída a largo plazo. "
            "Retención D7 ~86-87%; cae drásticamente en D14 y D28 (2-3%)."
        ),
        "implicacion": (
            "La mayoría de usuarios muestra interés inicial pero no permanece "
            "activo después de las primeras dos semanas."
        ),
    },
    "retencion_por_pais": {
        "hallazgo": (
            "México y Brasil tienen las mejores tasas de retención. "
            "Bolivia, Ecuador y Paraguay presentan las más bajas."
        ),
        "implicacion": (
            "Hay variabilidad por mercado. Se requiere estrategia diferenciada "
            "para mercados con retención baja."
        ),
    },
    "reflexion": {
        "etapa_a_mejorar": (
            "Transición 'Selección de ítem' → 'Añadir al carrito' "
            "(mayor caída porcentual en el embudo)."
        ),
        "aprendizaje": (
            "Los usuarios muestran alto interés inicial pero abandonan antes "
            "de añadir al carrito; la retención a largo plazo es el reto principal."
        ),
    },
}

# ─────────────────────────────────────────────
# VISUALIZACIONES
# ─────────────────────────────────────────────

def plot_embudo_general(df: pd.DataFrame) -> None:
    etapas = [
        "Select Item", "Add to Cart", "Begin Checkout",
        "Add Shipping", "Add Payment", "Purchase",
    ]
    valores = df.iloc[0].tolist()

    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(etapas, valores, color="#FFE600", edgecolor="#333333", linewidth=0.8)
    for bar, val in zip(bars, valores):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                f"{val:.2f}%", ha="center", va="bottom", fontsize=9, fontweight="bold")
    ax.set_title("Embudo de Conversión General — MercadoLibre 2025", fontsize=13, fontweight="bold")
    ax.set_ylabel("Tasa de conversión (%)")
    ax.set_ylim(0, max(valores) * 1.15)
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.1f%%"))
    plt.tight_layout()
    plt.savefig("embudo_general.png", dpi=150)
    plt.show()
    print("Guardado: embudo_general.png")


def plot_retencion_cohort(df: pd.DataFrame) -> None:
    dias = ["D7", "D14", "D21", "D28"]
    cols = ["retention_d7_pct", "retention_d14_pct", "retention_d21_pct", "retention_d28_pct"]
    colores = plt.cm.tab10.colors

    fig, ax = plt.subplots(figsize=(10, 6))
    for i, row in df.iterrows():
        lw = 2.5 if row["cohort"] == "Ago-2025" else 1.5
        ls = "--" if row["cohort"] == "Ago-2025" else "-"
        ax.plot(dias, row[cols].tolist(), marker="o", label=row["cohort"],
                color=colores[i % len(colores)], linewidth=lw, linestyle=ls)

    ax.set_title("Retención por Cohorte (D7–D28) — MercadoLibre 2025", fontsize=13, fontweight="bold")
    ax.set_ylabel("Retención (%)")
    ax.set_ylim(0, 100)
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.0f%%"))
    ax.legend(loc="upper right", fontsize=8)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig("retencion_cohort.png", dpi=150)
    plt.show()
    print("Guardado: retencion_cohort.png")


def plot_retencion_pais(df: pd.DataFrame) -> None:
    cols = ["retention_d7_pct", "retention_d14_pct", "retention_d21_pct", "retention_d28_pct"]
    dias = ["D7", "D14", "D21", "D28"]
    df_sorted = df.sort_values("retention_d7_pct", ascending=False).reset_index(drop=True)
    colores = plt.cm.tab10.colors

    fig, ax = plt.subplots(figsize=(10, 6))
    for i, row in df_sorted.iterrows():
        ax.plot(dias, row[cols].tolist(), marker="o", label=row["country"],
                color=colores[i % len(colores)], linewidth=1.8)

    ax.set_title("Retención por País (D7–D28) — MercadoLibre 2025", fontsize=13, fontweight="bold")
    ax.set_ylabel("Retención (%)")
    ax.set_ylim(0, 100)
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.0f%%"))
    ax.legend(loc="upper right", fontsize=8, ncol=2)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig("retencion_pais.png", dpi=150)
    plt.show()
    print("Guardado: retencion_pais.png")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("MERCADOLIBRE — RESUMEN EJECUTIVO")
    print("=" * 60)

    print("\n[1] Embudo General")
    print(embudo_general.to_string(index=False))

    print("\n[2] Embudo por País")
    print(embudo_pais.to_string(index=False))

    print("\n[3] Retención por País")
    print(retencion_pais.to_string(index=False))

    print("\n[4] Retención por Cohorte")
    print(retencion_cohort.to_string(index=False))

    print("\n[5] Hallazgos clave")
    for k, v in hallazgos.items():
        print(f"\n  [{k}]")
        for kk, vv in v.items():
            print(f"    {kk}: {vv}")

    print("\n[6] Generando gráficas...")
    plot_embudo_general(embudo_general)
    plot_retencion_cohort(retencion_cohort)
    plot_retencion_pais(retencion_pais)

    print("\n✅ Listo.")
