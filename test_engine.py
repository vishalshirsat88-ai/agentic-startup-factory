import sys
import os

sys.path.append(os.getcwd())
from agents.product_agent import ProductAgent
from agents.cto_agent import CTOAgent
from engine.file_generator import generate_backend_files

idea = {
    "name": "AI Email Tool",
    "description": "Personalizes emails"
}

product = ProductAgent().define_product(idea)
print("PRODUCT:", product)

arch = CTOAgent().design_architecture({
    "idea": idea,
    "product": product
})

print("ARCH:", arch)

generate_backend_files("test_project", arch)