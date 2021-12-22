.. TunAugmentor documentation master file, created by
   sphinx-quickstart on Mon Dec 20 12:57:16 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

TunAugmentor
========================================
**TunAugmentor** is a python library for image data augmentation.
Image augmentation is an effective technique widely used for Machine Learning and Computer Vision tasks.
The aim of image augmentation is to apply different transformations on existing images to create more data for the model hence increasing the performance of the model.
Therefore, it is the process of increasing the training dataset without collecting new data.

.. note::

   The aim of this project was to reimplement different image augmentation techniques using only Python and Numpy.
   We do not claim we reinvented the wheel. We know theese techniques are already available in different libraries with better implementations and you should probably use theese instead.
   The goal was to learn to implement this techniques and to try to distribute a Python Library. Thus, we didn't do any benchmarking for this work.

.. note::
   `Albumentations`_ was a great source of inspiration concerning which transformation to implement and for the documentation.
   Try to check their work you may find what you really need.

Installation:
#############


To use TunAugmentor, first install it using pip:

.. code-block:: console

   (.venv) $ pip install TunAugmentor

.. _Albumentations: https://github.com/albumentations-team/albumentations

.. toctree::
   :maxdepth: 2
   :caption: Contents:


   ./TunAugmentor.transformations.rst
   ./TunAugmentor.utils.rst
   ./TunAugmentor.pipeline.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
