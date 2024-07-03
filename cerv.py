from flask import Flask, request, render_template
from PIL import Image
import io
import torch
from torchvision.transforms import functional as F
from yolo import detect