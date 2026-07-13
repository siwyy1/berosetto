# Databricks notebook source
SOURCE_PATH = "abfss://bronze@newdatabucket.dfs.core.windows.net/e-commerce"

(
    spark.readStream
         .format("cloudFiles")
         .option("cloudFiles.format", "csv")
         .option("header", "true")
         .load(SOURCE_PATH)
         .writeStream
         .option("checkpointLocation", "/tmp/checkpoints/customers")
         .trigger(availableNow=True)
         .toTable("bronze.customers")
)